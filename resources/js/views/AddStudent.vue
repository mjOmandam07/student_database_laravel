<template>
    <h1 class="display-4 banner ml-5">{{ banner }}</h1>
    <div class="bg-light mr-auto ml-auto mt-4 mb-5 rounded table-div add-update">
        <form @submit.prevent="submit" class="container-fluid reg-form m-0 p-4">
          <legend class="lead display-4 mb-3">Register</legend>
          <div class="alert alert-success alert-dismissable m-1" v-show="success">
            <button type="button" class="close" data-dismiss="alert">×</button>
            Student Added Successfully
            </div>
            <div class="container-fluid form-row">
              <div class="form-group col-md-6 w-100">
                <label for="fnameInput" class="font-weight-bold">First Name</label>
                <input type="text" class="form-control"  placeholder="First Name" v-model="forms.firstName"/>
                <div class="invalid-feedback d-block" v-if="errors && errors.firstName">
                        <span>{{ errors.firstName[0] }}</span>
                </div>
              </div>
              <div class="form-group col-md-6 w-75">
                <label for="lnameInput" class="font-weight-bold">Last Name</label>
                <input type="text" class="form-control" placeholder="Last Name" v-model="forms.lastName" />
                <div class="invalid-feedback d-block" v-if="errors && errors.lastName">
                        <span>{{ errors.lastName[0] }}</span>
                </div>
              </div> 
            </div>
            <div class="container-fluid form-row">
              <div class="form-group w-25 col-md-2">
                <label for="genderSelect" class="font-weight-bold"
                  >Gender</label
                >
                <select class="form-control form-control-md" v-model="forms.gender">
                  <option selected disabled class="d-none" value="">Choose...</option>
                  <option value="Male">Male</option>
                  <option value="Female">Female</option>
                </select>
                <div class="invalid-feedback d-block" v-if="errors && errors.gender">
                        <span>{{ errors.gender[0] }}</span>
                </div>
              </div>
              <div class="form-group  col-md-3">
                <label for="iDInput" class="font-weight-bold">I.D Number</label>
                <input type="text" class="form-control form-control-md" placeholder="I.D Number" v-model="forms.id_number" />
                <div class="invalid-feedback d-block" v-if="errors && errors.id">
                        <span>{{ errors.id[0] }}</span>
                </div>
              </div>
              <div class="form-group col">
                <label for="lnameInput" class="font-weight-bold">College</label>
                <select class="form-control form-control-md" v-model="forms.college" @change="dynamicDept">
                  <option selected disabled class="d-none" value="">Select College</option>
                  <option v-for="college in colleges" :value="college.code" :key="college.id">({{ college.code }}) {{college.name}}</option>
                </select>
                <div class="invalid-feedback d-block" v-if="errors && errors.college">
                        <span>{{ errors.college[0] }}</span>
                </div>
              </div>   
            </div>
            <div class="container-fluid form-row">
              <div class="form-group col-3">
                <label for="yearSelect" class="font-weight-bold">Year Level</label>
                <select class="form-control form-control-md" v-model="forms.yearLevel">
                  <option selected disabled class="d-none" value="">Choose...</option>
                  <option v-for="yr in year" :value="yr" :key="yr">{{yr}}</option>
                  
                </select>
                <div class="invalid-feedback d-block" v-if="errors && errors.yearLevel">
                        <span>{{ errors.yearLevel[0] }}</span>
                </div>
              </div>
              <div class="form-group col">
                <label for="lnameInput" class="font-weight-bold">Department</label>
                <select class="form-control form-control-sm" v-model="forms.department" @change="dynamicCourse">
                  <option selected disabled value="">Select Department</option>
                  <option v-for="dept in departments" :value="dept.dept_id" :key="dept.dept_id">Department of {{dept.name}}</option>
                </select>
                <div class="invalid-feedback d-block" v-if="errors && errors.department">
                        <span>{{ errors.department[0] }}</span>
                </div>
              </div>
            </div>
            <div class="container-fluid form-row">
              <div class="form-group col">
                <label for="courseSelect" class="font-weight-bold"
                  >Course</label
                >
                <select class="form-control form-control-md" v-model="forms.course_code">
                  <option selected disabled class="d-none" value="">Select Course</option>
                  <option v-for="course in courses" :value="course.code" :key="course.id">({{ course.code }}) {{course.name}}</option>  
                </select>
                <div class="invalid-feedback d-block" v-if="errors && errors.course_code">
                        <span>{{ errors.course_code[0] }}</span>
                </div>
              </div>
            </div>
            <div class="container-fluid d-flex">
              <button class="btn w-25 btn-primary  ml-auto" type="submit">Add</button>
            </div>
        </form>
    </div>    
</template>
<script>
export default {
    props: {
        banner: String
    },
    data(){
        return {
            colleges: [],
            departments:[],
            courses:[],
            year : [1, 2, 3, 4, 5],
            forms : {
              firsName : null,
              lastName : null,
              gender : '',
              id_number : null,
              yearLevel: '',
              college: '',
              department: '',
              course_code:'',
            },
            success : false,
            errors : {}
      }
    },
    created() {
            const vm = this
            axios.get('http://localhost:8000/api/colleges')
            .then(function (response) {
              vm.colleges = response.data;
            });
    },
    computed : {
      dynamicDept(){
        this.forms.department = ''
        this.forms.course_code = ''
        const vm = this
        if (this.forms.college) {
          axios.get(`http://localhost:8000/api/dynamic/department/${this.forms.college}`)
            .then(function (response) {
              vm.departments = response.data;
            });
        }
      },
      dynamicCourse(){
        this.forms.course_code = ''
        const vm = this
        if (this.forms.department) {
          axios.get(`http://localhost:8000/api/dynamic/courses/${this.forms.department}`)
          .then(function (response) {
            vm.courses = response.data;
          })
        }
      }
    },

    methods: {
      submit () {
        const vm = this;
            axios.post('http://localhost:8000/api/add_student', this.forms)
            .then(function (response) {
              vm.forms.firstName = null
              vm.forms.lastName = null
              vm.forms.gender = ''
              vm.forms.id_number = null
              vm.forms.yearLevel = ''
              vm.forms.college = ''
              vm.forms.department = ''
              vm.forms.course_code = ''
              vm.success = true
              vm.errors = {}
              console.log(response.data)
            })
            .catch(function (error) {
                if (error.response.status == 422) {
                  vm.errors = error.response.data.errors;
                  if (vm.errors && vm.errors.first_name) {
                    console.log(vm.errors.first_name[0])
                  }
                }
                console.log(error);
            });
      }
    }

};
</script>
<style scoped>

</style>