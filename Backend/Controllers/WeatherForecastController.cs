using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Options;
using MongoDB.Driver;
using WebApi.Models;

namespace WebApi.Controllers;

[ApiController]
[Route("[controller]")]
public class WeatherForecastController : ControllerBase
{
    private static readonly string[] Summaries = new[]
    {
        "Freezing", "Bracing", "Chilly", "Cool", "Mild", "Warm", "Balmy", "Hot", "Sweltering", "Scorching"
    };

    private readonly IMongoCollection<SpeechesMetaData> _speechesMetaDataCollection;
    private readonly ILogger<WeatherForecastController> _logger;

    public WeatherForecastController(ILogger<WeatherForecastController> logger, IOptions<AustrianParliamentScrapeDatabaseSettings> austrianParliamentScrapeDatabaseSettings)
    {
        _logger = logger;
        var mongoClient = new MongoClient(
            austrianParliamentScrapeDatabaseSettings.Value.ConnectionString);

        var mongoDatabase = mongoClient.GetDatabase(
            austrianParliamentScrapeDatabaseSettings.Value.DatabaseName);

        _speechesMetaDataCollection = mongoDatabase.GetCollection<SpeechesMetaData>(
            austrianParliamentScrapeDatabaseSettings.Value.SpeechesMetaDataCollectionName);
    }

    [HttpGet(Name = "GetWeatherForecast")]
    public async Task<List<SpeechesMetaData>> Get()
    {
        return await _speechesMetaDataCollection.Find(_ => true).ToListAsync();
    }
}