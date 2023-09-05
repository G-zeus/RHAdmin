<template>
    <div>

        <Header/>
        <div class="container izquierda">

            <button class="btn btn-primary" v-on:click="nuevo()" >Nuevo Empleado</button>
            <br><br>


            <table class="table table-hover">
                <thead>
                <tr>
                    <th scope="col">ID</th>
                    <th scope="col">Nombre</th>
                    <th scope="col">APELLIDOS</th>
                    <th scope="col">PUESTO</th>
                    <th scope="col">FECHA ALTA</th>
                    <th scope="col">Estatus</th>
                </tr>
                </thead>
                <tbody>
                <tr v-for="employee in employeeList" :key="employee.id" v-on:click="editar(employee.id)">
                    <th scope="row">{{ employee.id}}</th>
                    <td>{{ employee.name }}</td>
                    <td>{{ employee.last_name + ' '+ employee.second_name}}</td>
                    <td>{{ employee.position }}</td>
                    <td>{{ employee.created_at }}</td>
                    <td>{{ employee.is_active ? 'Activo' : 'Baja' }}</td>
                </tr>

                </tbody>
            </table>

        </div>

        <Footer />
    </div>
</template>
<script>
import getEmployees from '@/modules/dashboard/helpers/getEmployees';
import Header from "@/modules/common/components/Header.vue";
export default {
    name:"Dashboard",
    data(){
        return {
            employeeList:null,
            pagina:1
        }
    },
    components: {
        Header,
    },

    methods:{
        editar(id){
            this.$router.push('/editarEmpleado/' + id);
        },
        nuevo(){
            this.$router.push('/nuevoEmpleado');
        }
    },
    mounted:function(){

        getEmployees().then(response =>{
            this.employeeList = response.data.data
        }).catch(error => {
            if (error.response.status === 401)
                this.$router.push('/login');

        });
    }
}
</script>
<style  scoped>
.izquierda{
    text-align: left;
}
</style>
