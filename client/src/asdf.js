import { useEffect, useState, useContext } from 'react'
import createContainer from 'constate'


const useApp = () => {
    const [foo, setFoo] = useState("bar")


    useEffect(() => {
        try {


        } catch (e) {
            console.log(e)
        }
    }, [])

    return {
        foo
    }
}

const { Context, Provider } = createContainer(useApp)

export const useAppState = () => {
    const state = useContext(Context)
    return state
}

export { Provider }
