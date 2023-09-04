import api from '@/modules/common/api/api'

const getEmployees = async () => {

  return await api.get('api/employee/'  ,{headers: {
    'Authorization': localStorage.getItem("tkn")
  }})

}

export default getEmployees
