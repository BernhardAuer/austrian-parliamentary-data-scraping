<script>
	// import SpeechTypeChart from './../components/SpeechTypeChart.svelte';
  import ChartService from './../services/chartService.js'

  let service = new ChartService();
  let dataToShow = '';
</script>

<h1>Willkommen bei deinem Info-Portal zu aktuellen Themen aus dem österreichischen Parlament.</h1>
<p>Test wir mal chart.js in der svelte edition:</p>

<!-- <SpeechTypeChart /> -->
<button on:click="{() => service.fetchSpeechMetaData((response) => dataToShow = response )}">API call!</button>
<button on:click="{() =>dataToShow= 'leer'}">löschen!</button>
<p>{dataToShow}</p>