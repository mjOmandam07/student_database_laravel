<template>
    <h1 class="display-4 banner ml-5">{{ what_college }}</h1>
    <div class="bg-light m-5 rounded table-div p-2">
        <div class="course-div container-fluid h-100 m-0 p-2">
                    <div class="row">
                        <div class="col-7">
                            <h1 class="display-6">Department of {{ current_dept }}</h1>
                        </div>
                        <div class="col-5 m-0 p-0">
                            <div class="row p-0 mr-2">
                               <div class="col-9">
                                    <select class="form-control" v-model="filters.department" @change="dynamicCourse">
                                    <option selected disabled value="">Select Department</option>
                                    <option v-for="dept in departments" v-bind:value="{id : dept.dept_id, name: dept.name}" :key="dept.dept_id">{{dept.name}}</option>
                                    </select>
                                </div>
                                <div class="col-3 d-flex">
                                    <select class="form-control form-control-md" v-model="filters.college" @change="dynamicDept">
                                        <option selected disabled value="">College</option>
                                        <option v-for="college in colleges" :value="college.code" :key="college.id">{{ college.code }}</option>  
                                    </select>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="row mt-2">
                        <table class="table table-borderless lead">
                            <tr  v-for="course in courses" :value="course.id" :key="course.id">
                                <td>({{ course.code }}) {{ course.name }}</td>
                            </tr>
                           
                            
                        </table>
                    </div>
                
                </div>
    </div>    
</template>
<script>
import { useRoute } from 'vue-router';
export default {
    data(){
        return {
            current_dept: '',
            what_college: '',
            colleges : [],
            departments : [],
            courses : [],
            filters: {
                college: '',
                department: ''
            }
        }
    },
    mounted() {
        this.whatCollege()
        this.dynamicDept();
        this.dynamicCollege();
        
    },
    computed: {
        
    },
    methods: {
        whatCollege (){
            const route = useRoute()
            const college_code = route.params.college
            this.what_college = college_code;
            this.filters.college = this.what_college
        },

        dynamicDept(){
            this.what_college = this.filters.college;
            this.filters.department = '';
            const vm = this
            axios.get(`http://localhost:8000/api/dynamic/department/${this.filters.college}`)
            .then(function (response) {
                vm.departments = response.data;
                vm.current_dept = vm.departments[0].name;
                vm.dynamicCourse(vm.departments[0].dept_id); 
                });
        },

        dynamicCollege() {
            const vm = this
            axios.get('http://localhost:8000/api/colleges')
            .then(function (response) {
              vm.colleges = response.data;
            });
        },
        dynamicCourse(dept){
            const vm = this
            if (this.filters.department) {
                axios.get(`http://localhost:8000/api/dynamic/courses/${this.filters.department.id}`)
                .then(function (response) {
                    vm.current_dept = vm.filters.department.name;
                    vm.courses = response.data;
                })
            } else {
                axios.get(`http://localhost:8000/api/dynamic/courses/${dept}`)
                .then(function (response) {
                    vm.courses = response.data;
                })
            }
      }
    },
};
</script>
<style scoped>
</style>