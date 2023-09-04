import api from '@/modules/common/api/api'

const getQRInfo = async (id) => {

  return await api.get(`/api/emergency/${id}`  ,{headers: {
  }})

}

export default getQRInfo
