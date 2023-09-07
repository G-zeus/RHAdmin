import api from '@/modules/common/api/api'

const getProfile = async () => {

  return await api.get(`api/profile`  ,{headers: {
    'Authorization': localStorage.getItem("tkn")
  }})

}

export default await getProfile().then(response =>{return true}).catch(error =>{return false})
