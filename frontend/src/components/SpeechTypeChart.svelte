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
        service.fetchSpeechTypes((response) => {
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
    populateData();
    
</script>
  <p>
    Folgende Grafik zeigt die Verteilung der Redebeitragsarten bei den Plenarsitzungen des Nationalrates (197. Sitzung).  
    <a href="https://www.parlament.gv.at/verstehen/glossare/abkuerzungen">Abkürzungsverzeichnis </a>
  </p>
  <div>
    {#if data != null}
     <Doughnut
     bind:chart
     width="100"
     height="300" {data} options={{ maintainAspectRatio: false }} />
     {/if}
</div>
  <button on:click="{() => populateData()}">draw grafics</button>