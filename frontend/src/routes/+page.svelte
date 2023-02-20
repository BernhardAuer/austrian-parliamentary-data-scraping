<script>
	import SpeechTypeChart from './../components/SpeechTypeChart.svelte';
	import ChartService from './../services/chartService.js';

	let service = new ChartService();
	let dataToShow = '';
</script>

	<SpeechTypeChart />
	<button on:click={() => service.fetchSpeechMetaData((response) => (dataToShow = response))}
		>API call!</button
	>
	<button on:click={() => (dataToShow = 'leer')}>löschen!</button>
	<p>{dataToShow}</p>

