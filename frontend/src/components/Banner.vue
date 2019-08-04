<template>
  <b-container>
  <div class="banner">
    <b-jumbotron bg-variant="transparent">
      <template slot="header">
        <h1><b>Hey! I'm Soumithri <br></b></h1>
        <h3>I'm a Full Stack Python Developer based in San Francisco.</h3>
      </template>

      <template slot="lead">
        Some of my skills include Python, Django, Flask, Vue.JS
      </template>
      <hr class="my-4">
      <p>
        HERE'S SOME OF MY WORK
      </p>
      <!-- <b-button variant="primary" href="#">Do Something</b-button>
      <b-button variant="success" href="#">Do Something Else</b-button> -->
    </b-jumbotron>
  </div>
  </b-container>
</template>

<script>
export default {
  name: 'Banner' //this is the name of the component
}
</script>
<style>

.banner {
  text-align: center;
}
</style>