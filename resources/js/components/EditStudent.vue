<template>
    <div class="modal-content">
        <div class="modal-header">
            <h2 class="modal-title" id="exampleModalLongTitle">Hello, {{ fname }}</h2>
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
                </div>
                <div class="form-group col-md-6 w-75">
                    <label for="lnameInput" class="font-weight-bold">Last Name</label>
                    <input type="text" class="form-control" placeholder="Last Name" v-model="edit_forms.lastName"/>
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
                </div>
                <div class="form-group  col-md-3">
                    <label for="iDInput" class="font-weight-bold">I.D Number</label>
                    <input type="text" class="form-control form-control-md" placeholder="I.D Number" v-model="edit_forms.id_number"/>
                </div>


                <div class="form-group col">
                    <label for="lnameInput" class="font-weight-bold">College</label>
                    <select class="form-control form-control-md" v-model="edit_forms.college"  @change="editDept">
                    <option selected disabled class="d-none" value="">Select College</option>
                    <option v-for="college in colleges" :value="college.code" :key="college.id">({{ college.code }}) {{college.name}}</option>
                    </select>
                </div>   
                </div>
                <div class="container-fluid form-row">
                <div class="form-group col-3">
                    <label for="yearSelect" class="font-weight-bold">Year Level</label>
                    <select class="form-control form-control-md" v-model="edit_forms.yearLevel">
                    <option selected disabled class="d-none" value="">Choose...</option>
                    <option v-for="yr in year" :value="yr" :key="yr">{{yr}}</option>         
                    </select>

                </div>
                <div class="form-group col">
                    <label for="lnameInput" class="font-weight-bold">Department</label>
                    <select class="form-control form-control-sm" v-model="edit_forms.department"  @change="editCourse">
                    <option selected disabled value="">Select Department</option>
                    <option v-for="dept in edit_departments" :value="dept.dept_id" :key="dept.dept_id">Department of {{dept.name}}</option>
                    </select>
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
                </div>
                </div>
                <div class="container-fluid d-flex">
                <button class="btn w-25 btn-primary m-1" type="submit">Update</button>
                 <button class="btn w-25 btn-danger m-1" type="submit">Delete</button>
                </div>
            </form>
        </div>
            
        </div>
</template>
<script>
export default {
    name : "EditStudent",
    props: {
        firstName : String,
        lastName : String,
        gender : String,
        id : String,
        yearLevel : Number,
        course_code : String,
        prop_colleges : Array
    },

    data () {
        return {
            fname : this.firstName,
            colleges : this.prop_colleges,
            edit_departments:[],
            edit_courses:[],
            year : [1, 2, 3, 4, 5],
            current_course : '',
            current_dept : '',
            current_college: '',
            edit_forms : {
              firstName : this.firstName,
              lastName : this.lastName,
              gender : this.gender,
              id_number : this.id_number,
              yearLevel: this.yearLevel,
              college: '',
              department: '',
              course_code:'',
            },
            success : false,
            errors : {}
        }
    }
    

}
</script>
