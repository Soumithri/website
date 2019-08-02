<template>
  <div class="home">
      <Banner />
      <ProjectList />
  </div>
</template>

<script>
// @ is an alias to /src
import ProjectList from '@/components/ProjectList.vue';
import Banner from '@/components/Banner.vue';

export default {
  name: 'home',
  components: {
    ProjectList,
    Banner,
  },
};
</script>

<style>


</style>

