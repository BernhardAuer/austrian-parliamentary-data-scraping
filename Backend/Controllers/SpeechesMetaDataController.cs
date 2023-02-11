using System;
using Microsoft.AspNetCore.Mvc;
using WebApi.DTOs;
using WebApi.Models;
using WebApi.Services;

namespace WebApi.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class SpeechesMetaDataController : ControllerBase
    {
        private readonly SpeechesMetaDataService _speechesMetaDataService;

        public SpeechesMetaDataController(SpeechesMetaDataService speechesMetaDataService) =>
            _speechesMetaDataService = speechesMetaDataService;
        
        [HttpGet]
        [Route("getTypeOfSpeechesCountList")]
        public async Task<List<TypeOfSpeechCountDto>> GetTypeOfSpeechesCountList()
        {
            var speechesCountList = await _speechesMetaDataService.GetTypeOfSpeechesCountList();
            // use automapper in the future
            var result = speechesCountList.Select(x => new TypeOfSpeechCountDto()
                {
                    TypeOfSpeech = x.TypeOfSpeech,
                    Count = x.Count
                })
                .OrderBy(x => x.TypeOfSpeech)
                .ToList();

            return result;
        }

        [HttpGet]
        public async Task<List<SpeechesMetaData>> Get() =>
            await _speechesMetaDataService.GetAsync();

        [HttpGet("{id:length(24)}")]
        public async Task<ActionResult<SpeechesMetaData>> Get(string id)
        {
            var book = await _speechesMetaDataService.GetAsync(id);

            if (book is null)
            {
                return NotFound();
            }

            return book;
        }

        [HttpPost]
        public async Task<IActionResult> Post(SpeechesMetaData newBook)
        {
            await _speechesMetaDataService.CreateAsync(newBook);

            return CreatedAtAction(nameof(Get), new { id = newBook.Id }, newBook);
        }

        [HttpPut("{id:length(24)}")]
        public async Task<IActionResult> Update(string id, SpeechesMetaData updatedBook)
        {
            var book = await _speechesMetaDataService.GetAsync(id);

            if (book is null)
            {
                return NotFound();
            }

            updatedBook.Id = book.Id;

            await _speechesMetaDataService.UpdateAsync(id, updatedBook);

            return NoContent();
        }

        [HttpDelete("{id:length(24)}")]
        public async Task<IActionResult> Delete(string id)
        {
            var book = await _speechesMetaDataService.GetAsync(id);

            if (book is null)
            {
                return NotFound();
            }

            await _speechesMetaDataService.RemoveAsync(id);

            return NoContent();
        }
        
    }
}
