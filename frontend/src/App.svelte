<script>
  import NoteCard from "./lib/NoteCard.svelte";

  // async function getNotes() {
  // const res = await fetch("http://127.0.0.1:8000");
  // const data = await res.json();
  // console.log(data);
  // }

  // getNotes();
</script>

<main class="max-w-4xl mx-auto p-5 arial">
  <h1 class="text-(xl gray-700) font-bold mb-5">Notes</h1>

  <!-- Display notes -->
  <section class="grid gap-5 md:grid-cols-3">
    {#each { length: 5 } as _}
      <NoteCard />
    {/each}
  </section>
</main>
