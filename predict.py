def shorten_text(text, max_char):
  while len(text) > max_char:
      text = ' '.join(text.split()[:-1]) + '…'
  return text
  
def predict(start):
  # get start sentence
  start = start.strip()

  try:
    # prepare input
    start_with_bos = '<|endoftext|>' + start
    encoded_prompt = trainer.tokenizer(start_with_bos, add_special_tokens=False, return_tensors="pt").input_ids
    encoded_prompt = encoded_prompt.to(trainer.model.device)

    # prediction
    output_sequences = trainer.model.generate(
      input_ids=encoded_prompt,
      max_length=160,
      min_length=10,
      temperature=1.,
      top_p=0.95,
      do_sample=True,
      num_return_sequences=10
      )
    generated_sequences = []

    # decode prediction
    for generated_sequence_idx, generated_sequence in enumerate(output_sequences):
      generated_sequence = generated_sequence.tolist()
      text = trainer.tokenizer.decode(generated_sequence, clean_up_tokenization_spaces=True, skip_special_tokens=True)
      if not ALLOW_NEW_LINES:
        limit = text.find('\n')
        text = text[: limit if limit != -1 else None]
      generated_sequences.append(text.strip())
    
    for i, g in enumerate(generated_sequences):
      predictions.append([start, g])
    
    for i, g in enumerate(generated_sequences):
      pred = start + ' → ' + g[len(start):].strip()
      print(pred)

  except Exception as e:
    print('\nAn error occured in predicting...\n')
    print(e)