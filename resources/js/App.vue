<template>
    <div>
        <nav class="navbar navbar-expand-lg navbar-dark mb-3">
            <div class="container-fluid">
                <a class="navbar-brand p-0" href="#">
                    <router-link :to="{name: 'Home'}">
                        <h3 class="mt-2">Student Database</h3>
                    </router-link>
                </a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                    <li class="nav-item">
                        
                            <a class="nav-link" aria-current="page" href="#">
                                <router-link :to="{name: 'Home'}">
                                    View All Students
                                </router-link>
                            </a>
                        
                    </li>
                    <li class="nav-item">
                        <router-link :to="{name: 'Add Student'}">
                            <a class="nav-link " aria-current="page" href="#">Add New Student</a>
                        </router-link>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link " aria-current="page" href="#">
                            <router-link :to="{name: 'Colleges'}">
                                Colleges
                            </router-link>
                        </a>
                    </li>
                    
                </ul>
                </div>
            </div>
        </nav>
        <router-view/>
    </div>
    
</template>


<script>

export default {
    
};

</script>
<style lang='scss' scoped>
    .navbar{
        a, .nav-link{
            color:white;

            &:hover{
                text-decoration:none;
                color:rgb(211, 210, 210);
            }
        }
    }
</style>