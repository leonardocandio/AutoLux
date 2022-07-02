<template>
  <nav>
    <router-link to="/" class="main-logo">AutoLux</router-link>
    <ul class="router-links">
      <li><router-link to="/forum">Forum</router-link></li>
    </ul>
  </nav>
  <router-view/>
</template>

<style>
*:not(i) {
  font-family: 'Roboto', sans-serif;
}
textarea {
  resize: none;
}

:root {
  --color-base: #f5f5f5;
  --color-background: #fff;
  --color-accent: #395e76;
}

body {
  height: 100%;
  margin: 0;
  display: flex;
  flex-direction: column;
  background-color: var(--color-base);
}

nav {
  position: -webkit-sticky;
  position: sticky;
  top: 0;
  height: 100px;
  background: var(--color-background);
  z-index: 1000;
  min-width: 580px;
  box-shadow: 0 0 3px 1px lightgray, 0 -3px 1px 1px lightgray;
}

ul {
  padding: 0;
  list-style-type: none;
}

li {
  margin: 5%;
}
h1 {
  color: black;
  font-size: 2.5em;
  font-weight: bold;
  border: 5px;
  padding: 15px;
}

#fragment {
  background-color: rgb(20, 18, 18);
}

h2 {
  color: #000;
  font-size: 2em;
  font-weight: bold;
}

h3 {
  color: #000;
  font-size: 1.5em;
  font-weight: bold;
}
a {
  text-decoration: none;
  color: var(--color-accent);
  font-weight: 600;
}

a:hover {
  cursor: pointer;
}

.main-logo {
  position: relative;
  float: left;
  height: 100px;
  line-height: 100px;
  padding: 0 15px;
  font-size: 22px;
  font-weight: 900;
  text-transform: uppercase;
}

.router-links {
  float: right;
  margin-right: 30px;
  position: relative;
}

nav .router-link :hover {
  color: #fff;
  background: var(--color-accent);
  border-radius: 2px;
}
nav .router-links li {
  list-style: none;
  position: relative;
  margin: 20px 20px 0;
  padding-bottom: 34px;
  display: inline-block;
}
nav .links li>router-link {
  position: relative;
  display: inline-block;
  padding: 0 20px;
  line-height: 30px;
  height: 30px;
}

nav .links li>router-link:hover {
  color: #fff;
  background: var(--color-accent);
  border-radius: 2px;
}

</style>
