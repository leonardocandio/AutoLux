<template>
  <div class="card">
    <p class="card-header" v-if="action==='login'">Ingresar</p>
    <p class="card-header" v-if="action==='register'">Registrarse</p>
    <div class="card-body">
      <FormKit
          type="form"
          id="auth-form"
          :actions="false"
          @submit="submitWrapper"

      >
        <FormKit type="text"
                 name="username"
                 placeholder="Nombre de usuario"
                 validation="required|min:3|max:20"
                 input-class="$reset form-control"
                 v-model="username"
                 v-if="action==='register'"
        />
        <FormKit type="text"
                 name="email"
                 placeholder="Correo electrónico"
                 validation="required|email"
                 input-class="$reset form-control"
                 v-model="email"
        />
        <FormKit type="password"
                 name="password"
                 placeholder="Contraseña"
                 validation="required"
                 input-class="$reset form-control"
                 v-model="password"
        />
        <FormKit type="submit"
                 label="Iniciar sesión"
                 input-class="$reset btn btn-submit"
        />
      </FormKit>
      <div class="card-footer">
        <ul class="auth-links">
          <li v-if="action==='login'">
            <a class="auth-link" href="/register">¿No tienes una cuenta?</a>
          </li>
          <li v-if="action==='register'">
            <a class="auth-link" href="/login">¿Ya tienes una cuenta?</a>
          </li>
          <li v-if="action==='login'">
            <a class="auth-link" href="/account-recovery">¿Olvidaste tu contraseña?</a>
          </li>
        </ul>
      </div>
    </div>
  </div>

</template>

<script>
export default {
  data(){
    return {
      username: '',
      email: '',
      password: '',
      res: {}
    }
  },
  name: "AuthForm",
  props: {
    action: {
      type: String,
      required: true
    }
  },
  methods: {
    async submitWrapper() {
      if (this.action === 'login') {
        await this.loginSubmit()
      } else if (this.action === 'register') {
        await this.registerSubmit()
      }
      if (this.res.code === 200) {
        router.push('/')
      } else {
        console.log(this.res.message)
      }
    },
    loginSubmit() {
      fetch('/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          email: this.email,
          password: this.password
        })
      }).then(response => {
        return response.json()
      }).then(data => {
        this.res = JSON.parse(JSON.stringify(data))
      }).catch(error => {
        console.log(error);
      });
    },
    registerSubmit() {
      fetch('/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          email: this.email,
          password: this.password,
          username: this.username
        })
      }).then(response => {
        return response.json()
      }).then(data => {
        this.res = JSON.parse(JSON.stringify(data))
      }).catch(error => {
        console.log(error);
      });
    }
  }
}
</script>

<style scoped>
.card {
  background-color: var(--color-background);
  width: 400px;
  height: 400px;
  margin: 7em auto;
  border-radius: 1.5em;
  box-shadow: 0 11px 35px 2px rgba(0, 0, 0, 0.14);
}

.card-header {
  padding-top: 12%;
  color: var(--color-accent);
  font-weight: bold;
  font-size: 23px;
  text-align: center;
}

.card-body {
  padding-top: 5%;
}

.card-footer {
  width: 100%;
  text-align: center;
}

.auth-links {
}

.auth-link {
  text-shadow: 0 0 3px rgba(117, 117, 117, 0.12);
  display: inline-block;
}
</style>
