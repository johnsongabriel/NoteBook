import extractorSvelte from "@unocss/extractor-svelte";
import {
  defineConfig,
  extractorSplit,
  presetIcons,
  presetUno,
  transformerDirectives,
  transformerVariantGroup
} from "unocss";

export default defineConfig({
  presets: [presetIcons(), presetUno()],
  extractors: [extractorSplit, extractorSvelte()],
  shortcuts: {
    container: "max-w-5xl mx-auto px-3",
  },
  transformers: [transformerDirectives(), transformerVariantGroup()]
});
