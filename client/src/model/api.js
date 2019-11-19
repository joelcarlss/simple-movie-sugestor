export const getUser = async () => {
  try {
    let data
    const result = await window.fetch('http://127.0.0.1:5002/users')
    if (result.status === 200) {
      data = await result.json()
    }
    return data.res
  } catch (e) {
    console.log(e)
    return undefined
  }
}

export const getData = async (id, amount, algoritm) => {
  try {
    let data
    const result = await window.fetch(`http://127.0.0.1:5002/find/movies/${algoritm}/${id}/${amount}`)
    if (result.status === 200) {
      data = await result.json()
    }
    console.log(data.res)
    return data.res
  } catch (e) {
    console.log(e)
    return undefined
  }
}

export const getReqUser = async (id, amount, algoritm) => {
  try {
    let data
    const result = await window.fetch(`http://127.0.0.1:5002/find/users/${algoritm}/${id}/${amount}`)
    if (result.status === 200) {
      data = await result.json()
    }
    console.log(data.res)
    return data.res
  } catch (e) {
    console.log(e)
    return undefined
  }
}