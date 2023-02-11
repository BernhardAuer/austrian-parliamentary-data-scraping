using Microsoft.Extensions.Options;
using MongoDB.Driver;
using WebApi.Models;

namespace WebApi.Services;

public class SpeechesMetaDataService
{
    private readonly IMongoCollection<SpeechesMetaData> _speechesMetaDataCollection;
    private readonly ILogger<SpeechesMetaDataService> _logger;

    public SpeechesMetaDataService(ILogger<SpeechesMetaDataService> logger, 
        IOptions<AustrianParliamentScrapeDatabaseSettings>  austrianParliamentScrapeDatabaseSettings)
    {
        var mongoClient = new MongoClient(austrianParliamentScrapeDatabaseSettings.Value.ConnectionString);
        var mongoDatabase = mongoClient.GetDatabase(austrianParliamentScrapeDatabaseSettings.Value.DatabaseName);

        _speechesMetaDataCollection = mongoDatabase
            .GetCollection<SpeechesMetaData>(austrianParliamentScrapeDatabaseSettings.Value.SpeechesMetaDataCollectionName);
        _logger = logger;
    }
    
    public async Task<List<SpeechesMetaData>> GetAsync() =>
        await _speechesMetaDataCollection.Find(_ => true).ToListAsync();

    public async Task<SpeechesMetaData?> GetAsync(string id) =>
        await _speechesMetaDataCollection.Find(x => x.Id == id).FirstOrDefaultAsync();

    public async Task CreateAsync(SpeechesMetaData newSpeechesMetaData) =>
        await _speechesMetaDataCollection.InsertOneAsync(newSpeechesMetaData);

    public async Task UpdateAsync(string id, SpeechesMetaData updatedSpeechesMetaData) =>
        await _speechesMetaDataCollection.ReplaceOneAsync(x => x.Id == id, updatedSpeechesMetaData);

    public async Task RemoveAsync(string id) =>
        await _speechesMetaDataCollection.DeleteOneAsync(x => x.Id == id);
    
}