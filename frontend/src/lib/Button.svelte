<script>
  /** @type {"button" | "reset" | "submit"} */
  export let type = "button";

  /** @type {string} */
  export let content = "Click Me";
</script>

<button
  on:click
  {type}
  class="{$$props.class} text-sm block border px-4 rounded py-1"
>
  {content}
</button>
