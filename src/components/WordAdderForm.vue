<script lang="ts" setup>
import { ref } from 'vue'
import { FwbInput, FwbSelect, FwbButton } from 'flowbite-vue'

// Input fields
const word = ref('')
const language = ref('')
const definition = ref('')
const position= ref('')
const category = ref('')
const preceding_words = ref('')
const following_words = ref('')
const synonyms = ref('')
const antonyms = ref('')
const example_sentences = ref('')
const notes = ref('')

// Options for select

interface FormData {
  value: string;
  name: string;
}


const positions: FormData[] = [
{value: 'noun', name: "noun"},
{value: 'adjective', name: "adjective"},
{value: 'adverb', name: "adverb"},
{value: 'pronoun', name: "pronoun"},
{value: 'preposition', name: "preposition"},
{value: 'conjunction', name: "conjunction"},
{value: 'interjection', name: "interjection"},
{value: 'determiner', name: "determiner"},
]

const languages: FormData[] = [
{value: 'English', name: "English"},
{value: 'French', name: "French"},
{value: 'Spanish', name: "Spanish"},
{value: 'Korean', name: "Korean"},
{value: 'Japanese', name: "Japanese"},
{value: 'Arabic', name: "Arabic"},
{value: 'Chinese', name: "Chinese"},
{value: 'German', name: "German"},
]
  

const showExtraOptions = ref(false)

</script>


<template>

  
  <div class="form-options flex justify-end"> 
      
     <fwb-button @click="showExtraOptions = !showExtraOptions" color="dark" >Options</fwb-button>
  </div>

  <form>
  <fwb-input
    wrapper-class="input-wrapper"
    v-model="word"
    placeholder="Enter the word"
    label="word"
  />

  <fwb-select
    class="input-wrapper"
    v-model="language"
    :options="languages"
    label="Select a language"
  />
  

  <fwb-select
    class="input-wrapper"
    v-model="position"
    :options="positions"
    label="Select a position"
  />


    <fwb-input
    wrapper-class="input-wrapper"
    v-model="definition"
    placeholder="Enter the definition"
    label="definition"
  />
  
  <div v-if="showExtraOptions" class="extra-options">
   <fwb-input
    wrapper-class="input-wrapper"
    v-model="preceding_words"
    placeholder="Enter the words that often precede this word separated by a comma"
    label="Preceding words"
  />

   <fwb-input
    wrapper-class="input-wrapper"
    v-model="following_words"
    placeholder="Enter the words that often follow this word separated by a comma"
    label="Following words"
    />

    <fwb-input
    wrapper-class="input-wrapper"
    v-model="synonyms"
    placeholder="Enter the words that often follow this word separated by a comma"
    label="Synonyms"
    />

    <fwb-input
    wrapper-class="input-wrapper"
    v-model="antonyms"
    placeholder="Enter the words that often follow this word separated by a comma"
    label="Antonyms"
    />

      
  </div>
  <fwb-button type="submit" color="dark">Submit</fwb-button>



  </form>

  

</template>


<style scoped>


  .input-wrapper {
    margin-bottom: 1rem;
  }
</style>