import { useEffect, useState, useContext } from 'react'
import createContainer from 'constate'
import { getUser, getData, getReqUser } from "./model/api"

const useApp = () => {
  const [users, setUsers] = useState([])
  const [name, setName] = useState('')
  const [amount, setAmount] = useState('')
  const [algoritm, setAlgoritm] = useState('')
  const [result, setResult] = useState([])
  const [userResult, setUserResult] = useState([])
  const [showUser, setShowUser] = useState(false)


  const updateResult = (showUser, name, amount, algoritm) => {
    if (name > 0 && algoritm.length > 0) {
      if (!showUser) {
        getReqUser(name, amount || 0, algoritm).then(r => setUserResult(r))
      } else {
        getData(name, amount || 0, algoritm).then(r => setResult(r))
      }
    }
    return name
  }

  useEffect(() => {
    try {
      getUser().then(u => { setUsers(u) })
    } catch (e) {
      console.log(e) // TODO: Show data from API instead?
    }
  }, [])

  return {
    users,
    name,
    setName,
    amount,
    setAmount,
    algoritm,
    setAlgoritm,
    result,
    updateResult,
    showUser,
    setShowUser,
    userResult,
    setUserResult
  }
}

const { Context, Provider } = createContainer(useApp)

export const useAppState = () => {
  const state = useContext(Context)
  return state
}

export { Provider }
