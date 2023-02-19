<script>
	import { TypeOfSpeechCountDto } from './../javascript-client-generated/src/model/TypeOfSpeechCountDto.js';
    import { Doughnut } from 'svelte-chartjs'; 
    import {
      Chart as ChartJS,
      Title,
      Tooltip,
      Legend,
      ArcElement,
      CategoryScale,
    } from 'chart.js'; 
    import ChartService from './../services/chartService.js'
  
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
                hoverBackgroundColor: ['#FF5A5E', '#5AD3D1', '#FFC870', '#A8B3C5', '#616774'],
            },
        ],
    };
    function populateData() {
        data = null;
        service.fetchSpeechTypes(selectedLegislatur, selectedMeetingNumber, inputTopNumber, selectedPoliticalParties, 
            (response) => {
                console.log("hahllo")
                console.log("raw:" + response);
                let typeOfSpeechCountList = Array.from(response, (element) =>{console.log("element:" + JSON.stringify(element)); return TypeOfSpeechCountDto.constructFromObject(element)});
                console.log("typed:" + JSON.stringify(typeOfSpeechCountList));
                dataTemplate.datasets[0].data = Array.from(typeOfSpeechCountList, (element) => element.count);
                dataTemplate.labels = Array.from(typeOfSpeechCountList, (element) => element.typeOfSpeech);
                console.log(dataTemplate);
                data = dataTemplate;
        });
    }
    let chart;
    let selectedLegislatur = 'XXVII';
    let selectedMeetingNumber = 197;
    let inputTopNumber = 'TOP 14-16';
	let selectedPoliticalParties = [];
    populateData();
    
</script>
  <p>
    Folgende Grafik zeigt die Verteilung der Redebeitragsarten bei den Plenarsitzungen des Nationalrates (197. Sitzung).
    <a href="https://www.parlament.gv.at/verstehen/glossare/abkuerzungen">Abkürzungsverzeichnis </a>
  </p>
  <div>
    <label for="legislatur">Gesetzgebungsperiode:</label><br>
    <select bind:value={selectedLegislatur} name="Gesetzgebungsperiode" id="legislatur">
        <option value="XXVII">XXVII</option>
        <option value="nix">nix</option>
    </select>
    <label for="meetingNumber">Sitzung:</label><br>
    <select bind:value={selectedMeetingNumber} name="Sitzung" id="meetingNumber">
        <option value=197>197</option> <option value=196>196</option>
    </select>
    <label for="topNumber">TOP:</label><br>
    <input bind:value={inputTopNumber} type="text" id="topNumber" name="TOP">

    <label for="topNumber">Partei:</label><br>
    <input type="checkbox" id="politicalParty_oevp" bind:group={selectedPoliticalParties} name="ÖVP" value="V">
    <label for="politicalParty_oevp">ÖVP</label><br>
    <input type="checkbox" id="politicalParty_spoe" bind:group={selectedPoliticalParties} name="SPÖ" value="S">
    <label for="politicalParty_spoe">SPÖ</label><br>
    <input type="checkbox" id="politicalParty_fpoe" bind:group={selectedPoliticalParties} name="FPÖ" value="F">
    <label for="politicalParty_fpoe">FPÖ</label>
    <input type="checkbox" id="politicalParty_gruene" bind:group={selectedPoliticalParties} name="GRÜNE" value="G">
    <label for="politicalParty_gruene">GRÜNE</label>
    <input type="checkbox" id="politicalParty_neos" bind:group={selectedPoliticalParties} name="NEOS" value="N">
    <label for="politicalParty_neos">NEOS</label>

    <p> {selectedLegislatur} {selectedMeetingNumber} {selectedPoliticalParties}</p>
  <button on:click="{() => populateData()}">draw grafics</button>
  </div>
  <div>
    {#if data != null}
     <Doughnut
     bind:chart
     width="100"
     height="300" {data} options={{ maintainAspectRatio: false }} />
     {/if}
</div>