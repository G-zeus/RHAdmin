import api from '@/modules/common/api/api'

const updateEmployee = async (id, data) => {

  return await api.patch(`api/employee/${id}`  , data,{headers: {
    'Authorization': localStorage.getItem("tkn")
  }})

}

export default updateEmployee
