<template>
  <div class="background"></div>

  <div class="outer-div">
    <div class="inner-div">
      <div class="front">
        <div class="">
          <h3 class=""> <font-awesome-icon icon="fa-solid fa-notes-medical" beat size="lg" /> Contacto de emergencia</h3>

          <div v-if="info_available">
            <p class="">
                <font-awesome-icon icon="fa-solid fa-user" />
              {{ emergency_contact }}
            </p>
            <p class=""><font-awesome-icon icon="fa-solid fa-phone" /> {{ emergency_phone }}</p>
            <p class=""><font-awesome-icon icon="fa-solid fa-droplet" /> {{ blood_type }}</p>
          </div>
            <p v-if="!info_available" class=""><i class="fas fa-phone front-icons"></i>Información no disponible</p>

        </div>
      </div>


    </div>
  </div>

</template>
<script>
import {FontAwesomeIcon, FontAwesomeLayersText} from "@fortawesome/vue-fontawesome";
import getQRInfo from "@/modules/emergency/helpers/getQRInfo";

export default {
  name: 'Info',
  components: {
    FontAwesomeIcon,
    FontAwesomeLayersText
  },
  data: function () {
    return {
      emergency_contact: null,
      emergency_phone: null,
      blood_type: "",
      info_available: false
    }
  },
  mounted: async function () {
    getQRInfo(this.$route.params.id)
        .then(data => {

          this.info_available = true
          this.emergency_contact = data.data.data.emergency_contact
          this.emergency_phone = data.data.data.emergency_phone
          this.blood_type = data.data.data.blood_type

        }).catch(error => {
      this.emergency_contact = ""
      this.emergency_phone = ""
      this.blood_type = ""
        console.log(error.response.data)

    })

  }


}
</script>
