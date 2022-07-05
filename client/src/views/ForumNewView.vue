<template>
  <div class="forum-new">
    <div class="form">
      <FormKit
          type="form"
          id="forum-new-form"
          :actions="false"
          @submit="submitPost"
      >
        <FormKit
            type="text"
            name="title"
            placeholder="Título"
            validation="required|length:3,20"
            input-class="$reset form-control"
            v-model="title"
        />
        <FormKit
            type="textarea"
            name="body"
            placeholder="Contenido"
            validation="required|length:3,1000"
            input-class="$reset form-control"
            v-model="body"
        />
        <FormKit
            type="submit"
            label="Publicar"
            input-class="$reset btn btn-submit"
        />
      </FormKit>
    </div>
  </div>
</template>

<script>
import router from "@/router";

export default {
  data() {
    return {
      title: '',
      body: '',
      res: {}
    }
  },
  name: "ForumNewView",
  methods: {
    async submitPost() {
      console.log("submitPost: " + this.title + " " + this.body);
      fetch('/posts/', {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          'post_title': this.title,
          'post_body': this.body
        })
      }).then(response => response.json())
          .then(async data => {
            this.res = JSON.parse(JSON.stringify(data));
            if (this.res.code === 200) {
              await router.push({name: "forum"});
            } else {
              alert(this.res.message);
            }
          })
          .catch(error => {
            console.log(error);
          });
    }
  }
}
</script>

<style scoped>
.forum-new {
  margin: auto;
}

.form {
  display: flex;
  flex-direction: column;
  width: 60%;
  margin: auto;
}

.form-title {
  margin: auto;
  background: var(--color-background);
  padding: 10px;
  border-radius: 1.5em;
}
</style>
