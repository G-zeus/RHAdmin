import api from '@/modules/common/api/api'

const getEmployee = async (id) => {

  return await api.get(`api/employee/${id}`  ,{headers: {
    'Authorization': localStorage.getItem("tkn")
  }})

}

export default getEmployee
