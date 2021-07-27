<template>
    <h1 class="display-4 banner ml-5">{{ banner }}</h1>
    <div class="bg-light m-5 rounded table-div">
       <div class="container-fluid college-view-tools m-0 mt-4">                 
          <div class="card-deck mr-2 ml-2">
            <router-link :to="{name: 'Courses', params:{college: 'COET'} }" tag="a">
              <a class="COET card text-white bg-none mb-3 mr-3 d-inline-block">
                <div class="card-body">
                  <h1 class="card-title display-2">COET</h1>
                  <p class="card-text lead">College of Engineering & Technology</p>
                </div>
              </a>
            </router-link>
            <router-link :to="{name: 'Courses', params:{college: 'CSM'} }" tag="a">
              <a class="card text-white bg-danger mb-3 d-inline-block">
                <div class="card-body">
                  <h1 class="card-title display-2">CSM</h1>
                  <p class="card-text lead">College of Science and Mathematics</p>
                </div>
              </a>
            </router-link>
          </div>
          <div class="card-deck mr-2 ml-2">
            <router-link :to="{name: 'Courses', params:{college: 'CCS'} }" tag="a">
              <a class="card text-white bg-primary mb-3 d-inline-block">
                <div class="card-body">
                  <h1 class="card-title display-2">CCS</h1>
                  <p class="card-text lead">College of Computer Studies</p>
                </div>
              </a>
            </router-link>
            <router-link :to="{name: 'Courses', params:{college: 'CED'} }" tag="a" >
              <a class="CED card text-white bg-none mb-3 d-inline-block">
                <div class="card-body">
                  <h1 class="card-title display-2">CED</h1>
                  <p class="card-text lead">College of Education</p>
                </div>
              </a>
            </router-link>
          </div>
          <div class="mr-2 ml-2 card-deck">
            <router-link :to="{name: 'Courses', params:{college: 'CASS'} }" tag="a">
              <a class="card text-white bg-success mb-3 d-inline-block">
                <div class="card-body">
                  <h1 class="card-title display-2">CASS</h1>
                  <p class="card-text lead">College of Arts and Social Science</p>
                </div>
              </a>
            </router-link>
            <router-link :to="{name: 'Courses', params:{college: 'CBAA'} }" tag="a">
              <a class="card text-white bg-warning mb-3 d-inline-block">
                <div class="card-body">
                  <h1 class="card-title display-2">CBAA</h1>
                  <p class="card-text lead">College of Business Administration & Accountancy</p>
                </div>
              </a>
            </router-link>
          </div>
          <div class="mr-2 ml-2 card-deck">
            <router-link :to="{name: 'Courses', params:{college: 'CON'} }" tag="a">
              <a class="card text-dark bg-light mb-3 d-inline-block border-secondary">
                <div class="card-body">
                  <h1 class="card-title display-2">CON</h1>
                  <p class="card-text lead">College of Nursing</p>
                </div>
              </a>
            </router-link>
          </div> 
        </div>
    </div>    
</template>
<script>
export default {
    props:{
      banner: String
    }
};
</script>
<style lang='scss' scoped>

.college-view-tools{
    .COET {
        background-color: #7b1113;

        &:hover{
            background-color: #660e10;
        }
    }

    .CED {
        background-color: #fb5581;

        &:hover{
            background-color: #d6456c;
        }
    }
    a{
      width:43vw;
      margin-left:auto;
      margin-right:auto;

    }
    a:hover{
        text-decoration:none;
    }
}
</style>
