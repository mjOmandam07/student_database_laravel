<template>
    <h1 class="display-4 banner ml-5">{{ banner }}</h1>
    <div class="bg-light m-5 rounded table-div p-4">
        <div class="row p-0 m-0">
            <div class="col row">
                  <select class="form-control form-control-md col mr-2" v-model="filter"  @change="filterStudent">
                  <option selected disabled class="d-none" value="">Filter by College</option>
                  <option v-for="college in colleges" :value="college.code" :key="college.id">({{ college.code }}) {{college.name}}</option>
                  </select>
                  <button class="btn btn-primary col-2" @click="viewStudents">Reset All</button>
              </div> 
            <div class="row col d-flex align-items-center justify-content-end">
                <input class="form-control mr-2 col-7" type="search" placeholder="Search" v-model="search" aria-label="Search">
                <button class="btn btn-primary col-2" type="submit" @click="searchStudent">Search</button>
            </div>
        </div>
        <table class="table table-hover mt-2">
            <thead>
                <th>Name</th>
                <th>I.D Number</th>
                <th>Course</th>
                <th>Year</th>
                <th>Actions</th>
            </thead>
            <tbody>
                <tr v-for="student in students" :key=student>
                    <td>{{ student.firstName }} {{ student.lastName }}</td>
                    <td>{{ student.id_number  }}</td>
                    <td>{{ student.course_code }}</td>
                    <td>{{ student.yearLevel }}</td>
                    <td>
                        <button class="btn btn-primary btn-sm mr-1" @click="edit(student)">View Data</button>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
    <div class="modal fade bd-example-modal-lg" id="editModal" tabindex="-1" role="dialog" aria-labelledby="myLargeModalLabel" aria-hidden="true">
      <div class="modal-dialog modal-lg">
        <div class="modal-content">
          <div class="modal-header">
            <h2 class="modal-title" id="exampleModalLongTitle">Hello, {{ current_firstName }}</h2>
              <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
        </div>
        <div class="modal-body">
            <form class="container-fluid reg-form m-0 p-4">
                <div class="container-fluid form-row">
                <div class="form-group col-md-6 w-100">
                    <label for="fnameInput" class="font-weight-bold">First Name</label>
                    <input type="text" class="form-control"  placeholder="First Name" v-model="edit_forms.firstName"/>
                    <div class="invalid-feedback d-block" v-if="errors && errors.firstName">
                        <span>{{ errors.firstName[0] }}</span>
                </div>
                </div>
                <div class="form-group col-md-6 w-75">
                    <label for="lnameInput" class="font-weight-bold">Last Name</label>
                    <input type="text" class="form-control" placeholder="Last Name" v-model="edit_forms.lastName"/>
                    <div class="invalid-feedback d-block" v-if="errors && errors.lastName">
                        <span>{{ errors.lastName[0] }}</span>
                    </div>
                </div> 
                </div>
                <div class="container-fluid form-row">
                <div class="form-group w-25 col-md-2">
                    <label for="genderSelect" class="font-weight-bold">
                        Gender
                    </label>
                    <select class="form-control form-control-md" v-model="edit_forms.gender">
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
                    <input type="text" class="form-control form-control-md" placeholder="I.D Number" v-model="edit_forms.id_number"/>
                    <div class="invalid-feedback d-block" v-if="errors && errors.id">
                        <span>{{ errors.id[0] }}</span>
                    </div>
                </div>


                <div class="form-group col">
                    <label for="lnameInput" class="font-weight-bold">College</label>
                    <select class="form-control form-control-md" v-model="edit_forms.college"  @change="editDept">
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
                    <select class="form-control form-control-md" v-model="edit_forms.yearLevel">
                    <option selected disabled class="d-none" value="">Choose...</option>
                    <option v-for="yr in year" :value="yr" :key="yr">{{yr}}</option>         
                    </select>
                    <div class="invalid-feedback d-block" v-if="errors && errors.yearLevel">
                          <span>{{ errors.yearLevel[0] }}</span>
                    </div>
                </div>
                <div class="form-group col">
                    <label for="lnameInput" class="font-weight-bold">Department</label>
                    <select class="form-control form-control-sm" v-model="edit_forms.department"  @change="editCourse">
                    <option selected disabled value="">Select Department</option>
                    <option v-for="dept in edit_departments" :value="dept.dept_id" :key="dept.dept_id">Department of {{dept.name}}</option>
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
                    <select class="form-control form-control-md" v-model="edit_forms.course_code">
                     <option selected disabled value="">Select Course</option>
                    <option v-for="course in edit_courses" :value="course.code" :key="course.id">({{ course.code }}) {{course.name}}</option>  
                    </select>
                    <div class="invalid-feedback d-block" v-if="errors && errors.course_code">
                        <span>{{ errors.course_code[0] }}</span>
                    </div>
                </div>
                </div>
                <div class="container-fluid d-flex">
                <button class="btn w-25 btn-primary m-1" type="submit" @click.prevent="updateStudent">Update</button>
                 <button class="btn w-25 btn-danger m-1" type="submit" @click.prevent="deleteStudent">Delete</button>
                </div>
            </form>
        </div>
            
        </div>
      </div>
    </div>    
</template>
<script>
export default {
    name : "Home",
    props: {
        banner: String,
    },
    data(){
        return {
            students:{},
            colleges: [],
            edit_departments:[],
            edit_courses:[],
            year : [1, 2, 3, 4, 5],
            current_firstName : '',
            current_id : '',
            current_course : '',
            current_dept : '',
            current_college: '',
            search : '',
            filter : '',
            edit_forms : {
              firsName : null,
              lastName : null,
              gender : '',
              id_number : null,
              yearLevel: '',
              college: '',
              department: '',
              course_code: '',
            },
            errors : {}
      }
    },
    mounted(){
        this.viewStudents()
    },  
    created() {
      this.viewColleges() 
    },
    methods: {
      viewStudents(){
        this.filter = ''
        this.search = ''
        const vm = this
        axios.get('http://localhost:8000/api/students')
        .then(function (response) {
        vm.students = response.data;
        });
      },
      viewColleges() {
        const vm = this
        axios.get('http://localhost:8000/api/colleges')
        .then(function (response) {
          vm.colleges = response.data;
        });
      },
      editDept(){
        this.edit_forms.department = ''
        const vm = this
        axios.get(`http://localhost:8000/api/dynamic/department/${this.edit_forms.college}`)
          .then(function (response) {
            vm.edit_departments = response.data;
          });

      },
      editCourse(){
        this.edit_forms.course_code = ''
        const vm = this
        axios.get(`http://localhost:8000/api/dynamic/courses/${this.edit_forms.department}`)
        .then(function (response) {
          vm.edit_courses = response.data;
        })

      },
      edit(item){
        $('#editModal').modal('show');
        console.log(item)
        this.edit_forms.firstName = item.firstName
        this.current_firstName = item.firstName
        this.edit_forms.lastName = item.lastName
        this.edit_forms.gender = item.gender
        this.edit_forms.id_number = item.id_number
        this.current_id = item.id_number
        this.edit_forms.yearLevel = item.yearLevel
        this.current_course = item.course_code
        this.currentCourse();
      },
      currentCourse(){
        const vm = this
        axios.get(`http://localhost:8000/api/editDynamic/course/${this.current_course}`)
          .then(function (response) {
            vm.current_dept = response.data[0].deptNo
            vm.currentDept();
          });   
      },
      currentDept(){
        const vm = this
        axios.get(`http://localhost:8000/api/editDynamic/department/${this.current_dept}`)
          .then(function (response) {
              const college = response.data[0].college_code
              vm.current_college = college
              vm.edit_forms.college = vm.current_college
              vm.editDept()
              vm.edit_forms.department = vm.current_dept
              vm.editCourse()
              vm.edit_forms.course_code = vm.current_course
          });
      },  
      deleteStudent(){
        const vm = this
        var verify = confirm("Student Will be Deleted")
        if (verify == true){
          axios.delete(`http://localhost:8000/api/delete_student/${this.current_id}`)
          .then(function (response) {
            $('#editModal').modal('hide');
            vm.viewStudents()
          });
        }
        
      },
      updateStudent(){
        const vm = this
        var verify = confirm("Student Will be Updated")
        if (verify == true){
          axios.put(`http://localhost:8000/api/update_student/${this.current_id}`, this.edit_forms)
          .then(function (response) {
            vm.errors = {}
            $('#editModal').modal('hide');
            vm.viewStudents()
          })
          .catch(function (error) {
                if (error.response.status == 422) {
                  vm.errors = error.response.data.errors;
                  if (vm.errors && vm.errors.first_name) {
                    console.log(vm.errors.first_name[0])
                  }
                }
                console.log(error);
            });;
        }
        
      },
      filterStudent(){
        const vm = this
        axios.get(`http://localhost:8000/api/get_students/${this.filter}`)
        .then(function (response) {
            vm.students = response.data;
            console.log(response.data)
        })
        .catch(function (error) {
            console.log(error);
          });
        
        
      },
      searchStudent(){
        const vm = this
        axios.get(`http://localhost:8000/api/search_students/${this.search}`)
        .then(function (response) {
            vm.students = response.data;
            console.log(response.data)
        })
        .catch(function (error) {
            console.log(error);
          });
        
        
      }
    }
};
</script>
<style scoped>
    
</style>