# AVIP 2026 — Task 1: Text Generation

**Repository name:** `GAI_1_TextGeneration_byte`  
**Task:** Text Generation  
**Generated samples:** 20  
**Prompt diversity:** educational explanations, environmental awareness, science, AI, cybersecurity, future technology, programming, reasoning, decision-making, mathematics, critical thinking, fiction, world-building, dialogue, alternative history, professional writing, summarization, structured planning, and audience adaptation.

## Project overview

This repository contains the 20 prompts used for the text-generation task and the corresponding text responses. Each response is stored as a separate UTF-8 `.txt` file in `generated_samples/`. File numbering follows the prompt numbering in `prompts.txt`.

## Model and source

- **Model label used for these samples:** GPT-6, through the hosted ChatGPT interface.
- **Inference method used for the submitted samples:** prompts were entered into the ChatGPT interface and the returned answers were saved as text files. The provided optional API example was **not** used to produce these original sample files.
- **Local checkpoint:** none. No model weights are included in this repository.
- **Official model documentation:** https://developers.openai.com/api/docs/models
- **ChatGPT model availability information:** https://help.openai.com/en/articles/20001354-gpt-6-and-other-models-in-chatgpt
- **Terms / output rights reference:** https://openai.com/policies/row-terms-of-use/

GPT-6 is a hosted model, not an open-weight checkpoint distributed with this project, so this repository does not claim an open-source model license. Review the official terms and any applicable institutional or assignment rules before redistributing or using the samples. The exact backend snapshot, decoding settings, and token-level probabilities were not exposed in the chat interface and are not asserted here.

## Repository contents

```text
GAI_1_TextGeneration_byte/
├── README.md
├── prompts.txt
├── evaluation_summary.md
├── inference_example.py
├── requirements.txt
└── generated_samples/
    ├── 01_sky-colour-and-sunset.txt
    ├── 02_reduce-plastic-on-campus.txt
    ├── ...
    └── 20_cloud-computing-two-audiences.txt
```

There are 20 separate generated sample files. The ellipsis above is only for readability in this overview; all 20 files are included in the archive.

## How to review the samples

1. Read `prompts.txt` to see the exact prompt list.
2. Open the correspondingly numbered file in `generated_samples/` to review each answer.
3. Read `evaluation_summary.md` for the qualitative assessment (under 300 words).

## Optional inference example

`inference_example.py` demonstrates how to submit a prompt to the OpenAI Responses API if you later wish to try API-based generation. This is an optional reproduction example, **not the method used to generate the sample files in this repository**. It requires an OpenAI API account, API access to the selected model, and applicable API billing. No API key is included in the repository.

Install the SDK:

```bash
python -m pip install -r requirements.txt
```

Set your API key through an environment variable, then run a prompt:

**macOS / Linux**

```bash
export OPENAI_API_KEY="your-api-key"
python inference_example.py "Explain recursion to a beginner using a simple example."
```

**Windows PowerShell**

```powershell
$env:OPENAI_API_KEY = "your-api-key"
python inference_example.py "Explain recursion to a beginner using a simple example."
```

The script uses `OPENAI_MODEL` if set; otherwise it defaults to `gpt-6-luna`. An API model may differ from the model serving a ChatGPT conversation. See the official model documentation for current API model IDs and availability.

## Evaluation

See [`evaluation_summary.md`](evaluation_summary.md). The repository uses a qualitative review rather than reporting BLEU or perplexity values because no reference corpus, scoring pipeline, or model log-probabilities were available for these hosted-interface outputs.
