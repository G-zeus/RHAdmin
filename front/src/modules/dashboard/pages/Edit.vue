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
        <div>
          <label></label>
        </div>


        <div class="form-group">
          <button type="button" class="btn btn-primary" v-on:click="validate()">Editar</button>
          <button type="button" class="btn btn-danger margen" v-on:click="deactivate()" v-if="is_active">Dar de baja
          </button>
          <button type="button" class="btn btn-danger margen" v-on:click="activate()" v-if="!is_active">Dar de Alta
          </button>
          <a type="button" class="btn btn-info margen" v-on:click.prevent="qr()">Descargar QR</a>
          <button type="button" class="btn btn-dark margen" v-on:click="back()">Salir</button>
        </div>
      </form>
    </div>
    <div v-if="bagError[0]">
      {{ bagError[0].message }}
    </div>
  </div>

  <div class="container izquierda">

    <br><br>

    <div>
      <label><strong>Historial de cambios </strong></label>
    </div>

    <table class="table table-hover">
      <thead>
      <tr>
        <th scope="col">Cambios</th>
        <th scope="col">Fecha</th>
      </tr>
      </thead>
      <tbody>
      <tr v-for="h in history" :key="h.id">
        <td>{{ h.values }}</td>
        <td>{{ h.created_at }}</td>
      </tr>

      </tbody>
    </table>

  </div>

</template>
<script>
import Header from '@/modules/common/components/Header.vue';
import getEmployee from '@/modules/dashboard/helpers/getEmployee'
import deleteEmployee from '@/modules/dashboard/helpers/deleteEmployee'
import updateEmployee from '@/modules/dashboard/helpers/updateteEmployee'

export default {
  name: "Edit",
  components: {
    Header,
    //Footer
  },
  data: function () {
    return {
      name: null,
      last_name: null,
      second_name: null,
      position: "",
      emergency_contact: null,
      emergency_phone: null,
      blood_type: "",
      is_active: null,
      history: [],
      bagError: []
    }
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


      this.edit()


    },

    edit() {
      const {history, bagError, ...data} = this.$data
      updateEmployee(this.$route.params.id, data).then(data => {
            this.$router.push("/dashboard");

          }
      ).catch(e => {
        this.bagError.push({
          'message': e.response.msg

        });
      })
    },
    back() {
      this.$router.push("/dashboard");
    },
    deactivate() {
      deleteEmployee(this.$route.params.id).then(data => {
            this.$router.push("/dashboard");

          }
      ).catch(e => {
        this.bagError.push({
          'message': e.response.msg

        });
      })


    },
    activate() {
      updateEmployee(this.$route.params.id, {'is_active': true}).then(data => {
            this.$router.push("/dashboard");

          }
      ).catch(e => {
        this.bagError.push({
          'message': e.response.msg

        });
      })


    },
    qr() {
      window.location.href = process.env.VUE_APP_API_URL + 'api/emergency/qr/' + this.$route.params.id

    }
  },
  mounted: async function () {

    getEmployee(this.$route.params.id)
        .then(data => {

          this.name = data.data.data.name
          this.last_name = data.data.data.last_name
          this.second_name = data.data.data.second_name
          this.position = data.data.data.position
          this.emergency_contact = data.data.data.emergency_contact
          this.emergency_phone = data.data.data.emergency_phone
          this.blood_type = data.data.data.blood_type
          this.is_active = data.data.data.is_active
          this.history = data.data.data.history

        })
        .catch(error => {
            if (error.response.status === 401){
                console.log(error.response)

                this.$router.push('/login');
                return false
            }

            this.bagError.push({

            'message': e.response.msg

          });

        });

  }
}
</script>
<style scoped>
.left {
  text-align: left;
}

.margen {
  margin-left: 15px;
  margin-right: 15px;
}
</style>
