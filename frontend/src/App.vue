<template>
  <div id="app">
    <div id="nav">
      <b-container>
        <b-nav justified>
          <b-nav-item active>
            <router-link to="/">Home</router-link>
          </b-nav-item>
         
          <!-- <b-nav-item>
            <router-link to="/posts">Blogs</router-link>
          </b-nav-item> -->
         
          <b-nav-item>
            <router-link to="/about">About</router-link>
          </b-nav-item>
          
          <b-nav-item>Resume</b-nav-item>
          <b-nav-item>Contact</b-nav-item>
        </b-nav>
        <hr class="my-4">
      </b-container>
    </div>
    <router-view/>
  </div>
</template>

<script>
import Banner from '@/components/Banner.vue';
export default {
  components: {
    Banner,
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  padding-bottom: 30px;
}
#nav {
  padding-top: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
