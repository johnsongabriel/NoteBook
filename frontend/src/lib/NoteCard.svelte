<script>
  import dayjs from "dayjs";
  import Button from "./Button.svelte";

  export let note = {};
</script>

<div class="shadow-md border p-5 rounded">
  <h2 class="text-gray-700 font-bold">{note.title}</h2>
  <p class="text-(xs gray-400) italic mb-2">
    Created on {dayjs(note.date).format("DD MMMM, YYYY - HH:mm A")}
  </p>
  <p class="text-(sm gray-500)">{note.descr}</p>

  <div class="flex justify-between items-center mt-5">
    <Button content="Edit" class="text-blue border-blue/40" />
    <Button content="Delete" class="text-red border-red/40" />
  </div>
</div>
