<template>
  <div>
    <h1> These are posts</h1>
    <div v-for="(post, id) in posts" :key="id"> 
        <h2>{{ post.title }}</h2>
        <p>{{ post.content }}</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      posts: [],
    };
  },
  mounted() {
    this.fetchPosts();
    document.title = 'Posts';
  },
  methods: {
    fetchPosts() {
        fetch('http://localhost:8000/api/posts/', {
          method: 'get',
          headers: {
              Accept: 'application/json',
          },
        })
          .then((response) => { return response.json(); })
          .then((jsonData) => {
            this.posts = jsonData.results;
          });
    },
  },
};
</script>
