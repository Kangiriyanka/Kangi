
### API
State that can trigger updates when changed is considered reactive. We can declare reactive state using Vue's reactive() API.


Bind an attribute to dynamic value
- v-bind:id="" or :id or :class

```vue
<script setup>
import { ref } from 'vue'

const titleClass = ref('title')
</script>

<template>
  <h1 :class="titleClass">Make me red</h1>
</template>

<style>
.title {
  color: red;
}
</style>

```

Event Listeners
```vue
<button v-on:click="increment">{{ count }}</button>
<button @click="increment">{{ count }}</button>
```

Two way bindings
```vue

function onInput(e) {
  // a v-on handler receives the native DOM event
  // as the argument.
  text.value = e.target.value

  v-model
}

<input :value="text" @input="onInput">
<input v-model="text">
```


Conditional rendering

```vue
<h1 v-if="awesome">Vue is awesome!</h1>
<h1 v-else>Oh no 😢</h1>
```

```vue

<script setup>
import { ref } from 'vue'

const awesome = ref(true)

function toggle() {
  awesome.value = !awesome.value
}
</script>

<template>
  <button @click="toggle">Toggle</button>
  <h1 v-if="awesome">Vue is awesome!</h1>
  <h1 v-else>Oh no 😢</h1>
</template>

```

List Rendering

```
<ul>
  <li v-for="todo in todos" :key="todo.id">
    {{ todo.text }}
  </li>
</ul>
```
