import api from '@/modules/common/api/api'

const apiLogin = async (data) => {
  console.log(data)

  return await api.post('api/login',data )

}

  export default apiLogin
