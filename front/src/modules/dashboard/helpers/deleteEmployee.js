import api from '@/modules/common/api/api'

const deleteEmployee = async (id) => {

  return await api.delete(`api/employee/${id}`  ,{headers: {
    'Authorization': localStorage.getItem("tkn")
  }})

}

export default deleteEmployee
