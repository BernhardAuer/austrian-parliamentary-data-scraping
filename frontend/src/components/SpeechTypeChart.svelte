<script>
	import { TypeOfSpeechCountDto } from './../javascript-client-generated/src/model/TypeOfSpeechCountDto.js';
	import { Doughnut } from 'svelte-chartjs';
	import { Chart as ChartJS, Title, Tooltip, Legend, ArcElement, CategoryScale } from 'chart.js';
	import ChartService from './../services/chartService.js';

	ChartJS.register(Title, Tooltip, Legend, ArcElement, CategoryScale);
	let service = new ChartService();
	let speechTypes = new TypeOfSpeechCountDto();

	let data = null;

	let dataTemplate = {
		labels: [],
		datasets: [
			{
				data: [],
				backgroundColor: ['#F7464A', '#46BFBD', '#FDB45C', '#949FB1', '#4D5360'],
				hoverBackgroundColor: ['#FF5A5E', '#5AD3D1', '#FFC870', '#A8B3C5', '#616774']
			}
		]
	};
	function populateData() {
		data = null;
		service.fetchSpeechTypes(
			selectedLegislatur,
			selectedMeetingNumber,
			inputTopNumber,
			selectedPoliticalParties,
			(response) => {
				console.log('hahllo');
				console.log('raw:' + response);
				let typeOfSpeechCountList = Array.from(response, (element) => {
					console.log('element:' + JSON.stringify(element));
					return TypeOfSpeechCountDto.constructFromObject(element);
				});
				console.log('typed:' + JSON.stringify(typeOfSpeechCountList));
				dataTemplate.datasets[0].data = Array.from(
					typeOfSpeechCountList,
					(element) => element.count
				);
				dataTemplate.labels = Array.from(typeOfSpeechCountList, (element) => element.typeOfSpeech);
				console.log(dataTemplate);
				data = dataTemplate;
			}
		);
	}
	let chart;
	let selectedLegislatur = 'XXVII';
	let selectedMeetingNumber = '197';
	let inputTopNumber = 'TOP 14-16';
	let selectedPoliticalParties = ['V', 'S', 'F', 'G', 'N'];
	populateData();
</script>

<h1 class="text-5xl font-normal leading-normal mt-0 mb-2 text-blue-800">
	TypeOfSpeech Grafik der Parlamentsreden
</h1>
<p class="text-1xl  leading-tight mt-0 mb-2">
	Folgende Grafik zeigt die Verteilung der Redebeitragsarten bei den Plenarsitzungen des
	Nationalrates. Benützen Sie den Filter, um die Datengrundlage der Grafik zu verändern.

	<a class="link" href="https://www.parlament.gv.at/verstehen/glossare/abkuerzungen"
		>Abkürzungsverzeichnis
	</a>
</p>
<div class="flex gap-x-4 gap-y-4 flex-wrap">
<div class="card w-fit bg-base-100 shadow-xl">
	<div class="card-body">
		<h2 class="card-title">Datenfilter</h2>
		<div>
			<label class="block text-gray-700 text-sm font-bold mb-2" for="legislatur"
				>Gesetzgebungsperiode:</label
			>
			<select
				class="select select-bordered w-full max-w-xs"
				bind:value={selectedLegislatur}
				name="Gesetzgebungsperiode"
				id="legislatur"
			>
				<option value="XXVII">XXVII</option>
				<option value="nix">nix</option>
			</select>
		</div>
		<div>
			<label class="block text-gray-700 text-sm font-bold mb-2" for="meetingNumber">Sitzung:</label>
			<select class="select select-bordered w-full max-w-xs" bind:value={selectedMeetingNumber} name="Sitzung" id="meetingNumber">
				<option value="197">197</option> <option value="196">196</option>
			</select>
        
		</div>
		<div>
			<label class="block text-gray-700 text-sm font-bold mb-2" for="topNumber">TOP:</label>
			<input placeholder="Suche nach Top-Nr / Thema" class="input input-bordered w-full max-w-xs" bind:value={inputTopNumber} type="text" id="topNumber" name="TOP" />
		</div>
		<div>
			<label class="block text-gray-700 text-sm font-bold mb-2" for="topNumber">Partei:</label>
			<input                
				type="checkbox"
				class="checkbox"
				id="politicalParty_oevp"
				bind:group={selectedPoliticalParties}
				name="ÖVP"
				value="V"
                
			/>
			<label for="politicalParty_oevp">ÖVP</label>
			<input
				type="checkbox"
				class="checkbox"
				id="politicalParty_spoe"
				bind:group={selectedPoliticalParties}
				name="SPÖ"
				value="S"
			/>
			<label for="politicalParty_spoe">SPÖ</label>
			<input
				type="checkbox"
				class="checkbox"
				id="politicalParty_fpoe"
				bind:group={selectedPoliticalParties}
				name="FPÖ"
				value="F"
			/>
			<label for="politicalParty_fpoe">FPÖ</label>
			<input
				type="checkbox"
				class="checkbox"
				id="politicalParty_gruene"
				bind:group={selectedPoliticalParties}
				name="GRÜNE"
				value="G"
			/>
			<label for="politicalParty_gruene">GRÜNE</label>
			<input
				type="checkbox"
				class="checkbox"
				id="politicalParty_neos"
				bind:group={selectedPoliticalParties}
				name="NEOS"
				value="N"
			/>
			<label for="politicalParty_neos">NEOS</label>
		</div>
		<button class="btn " on:click={() => populateData()}>draw grafics</button>
	</div>
</div>

<div />

<div class="card w-fit bg-base-100 shadow-xl">
	<div class="card-body">
        <div>
		<h2 class="card-title">Type of Speech Diagramm</h2>
     
		<Doughnut bind:chart {data} options={{responsive: true  }} />
	</div>
    </div>
</div>

	
</div>
