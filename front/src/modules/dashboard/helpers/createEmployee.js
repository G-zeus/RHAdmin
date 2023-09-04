import api from '@/modules/common/api/api'

const createEmployee = async (data) => {

  return await api.post('api/employee/'  , data,{headers: {
    'Authorization': localStorage.getItem("tkn")
  }})

}

export default createEmployee
