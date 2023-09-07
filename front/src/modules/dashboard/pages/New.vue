<template>
  <div>
    <Header/>
    <div class="container">


      <form action="" class="form-horizontal">

        <div>
          <label><strong>Información general </strong></label>
        </div>

        <div class="form-group left row">
          <div class="col">
            <label for="" class="control-label col-sm-3">Nombre(s) *</label>
            <div class="col-sm-7">
              <input type="text" class="form-control" name="name" id="name" v-model="name">
            </div>
          </div>
          <div class="col">
            <label for="" class="control-label col-sm-5">Primer Apellido *</label>
            <div class="col-sm-7">
              <input type="text" class="form-control" name="last_name" id="last_name" v-model="last_name">
            </div>
          </div>
        </div>
        <div class="form-group left row">
          <div class="col">
            <label for="" class="control-label col-sm-2">Segundo apellido *</label>
            <div class="col-sm-7">
              <input type="text" class="form-control" name="second_name" id="second_name" v-model="second_name">
            </div>
          </div>
          <div class="col">
            <label for="" class="control-label col-sm-2">Puesto</label>
            <div class="col-sm-7">
              <input type="text" class="form-control" name="position" id="position" v-model="position">
            </div>
          </div>
        </div>

        <div>
          <label><strong>Información de emergencia </strong></label>
        </div>

        <div class="form-group left">
          <label for="" class="control-label col-sm-2">Contacto de emergencia *</label>
          <div class="col-sm-10">
            <input type="text" class="form-control" name="emergency_contact" id="emergency_contact"
                   v-model="emergency_contact">
          </div>
        </div>

        <div class="form-group left row ">
          <div class="col">
            <label for="" class="control-label col-sm-2">Teléfono de emergencia *</label>
            <div class="col-sm-7">
              <input type="text" class="form-control" name="emergency_phone" id="emergency_phone"
                     v-model="emergency_phone">
            </div>
          </div>
          <div class="col">
            <label for="" class="control-label col-sm-2">Tipo de sangre</label>
            <div class="col-sm-7">
              <input type="text" class="form-control" name="blood_type" id="blood_type" v-model="blood_type">
            </div>
          </div>
        </div>


        <div class="modal-footer">
          <button type="button" class="btn btn-primary" v-on:click="validate()">Guardar</button>
          <button type="button" class="btn btn-secondary" v-on:click="back()">Salir</button>
        </div>
      </form>


    </div>
    <div v-if="bagError[0]">
      {{ bagError[0].message }}
    </div>
  </div>
</template>
<script>
import Header from '@/modules/common/components/Header.vue'
//import Footer from '@/components/Footer.vue'
import createEmployee from '@/modules/dashboard/helpers/createEmployee';

export default {
  name: "New",
  data: function () {
    return {
      name: null,
      last_name: null,
      second_name: null,
      position: "",
      emergency_contact: null,
      emergency_phone: null,
      blood_type: "",
      bagError: []
    }
  },
  components: {
    Header,
  },
  methods: {
    validate() {
      this.bagError = []
      if (!this.name || !this.name.trim()) {
        this.bagError.push({
          'message': 'Nombre es requerido y no puede contener solo espacios en blanco'
        });

        return false
      }
      if (!this.last_name || !this.last_name.trim()) {

        this.bagError.push({
          'message': 'Primer apellido es requerido y no puede contener solo espacios en blanco'
        });

        return false
      }
      if (!this.second_name || !this.second_name.trim()) {

        this.bagError.push({
          'message': 'Segundo apellido es requerido y no puede contener solo espacios en blanco'
        });

        return false
      }
      if (!this.emergency_contact || !this.emergency_contact.trim()) {

        this.bagError.push({
          'message': 'Contacto de emergencia es requerido y no puede contener solo espacios en blanco'
        });

        return false
      }
      if (!this.emergency_phone || !this.emergency_phone.trim()) {

        this.bagError.push({
          'message': 'Telefono de emergencia es requerido y no puede contener solo espacios en blanco'
        });

        return false
      }


      this.save()


    },

    save() {
      const {bagError, ...data} = this.$data

      createEmployee(data)
          .then(data => {
            this.$router.push("/dashboard");
          }).catch(e => {
        this.bagError.push({
          'message': e.response.msg

        });

      })
    },
    back() {
      this.$router.push("/dashboard");
    },


  }
}
</script>
<style scoped>
.left {
  text-align: left;
}
</style>
