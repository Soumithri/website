<<template>
	<b-container>
  <div class="ProjectList">
				<b-row no-gutters class="justify-content-md-center">
					<div :key="id" v-for="(post, id) in posts">
						<b-col l="4">
							<b-card
								v-bind:title="post.title"
								v-bind:img-src="post.project_img"
								img-alt="Image"
								img-top
								tag="article"
								class="mb-5 overflow-hidden border-0 card">
								<b-card-text>{{ `${post.description.slice(0,100)}...` }}</b-card-text>
								<b-card-body>
									<a :href="post.github_link" class="card-link">github link</a>
								</b-card-body>
								<b-button href="#" variant="outline-dark">Read More</b-button>
							</b-card>
						</b-col>
					</div>
				</b-row>
			</div>
	</b-container>
</template>

<script>
export default {
	name: 'ProjectList',
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
		fetch('http://localhost/api/projects/', {
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

<style>
.ProjectDetail {
	padding-top: 10px;
}

.card {
	max-width: 20rem;
  object-fit: cover;
}

.ProjectDetail b-card-group {
	padding: 100px;
}
</style>
