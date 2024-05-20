# 🤖 LLM-based Multi-agent quick tour 🤖

Source code used in "INTELLIGENT COLLABORATION - MULTI-AGENT LLM FOR DRIVING INNOVATION" webinar.

# Google Colab links

- AutoGen Quick Tutorial: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1AQVulyKLqi2d6v2HtcYgpE9pP7v8PXgu?usp=sharing)

- crewAI Quick Tutorial: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1bwJEel6jf8hYGE66wmY9KEzmgZrKSy2x?usp=sharing)


# Installation

The current code runs with Python 3.10.14. Run the below command to install all necessary libraries:

```bash
pip install -r requirements.txt
```

To use local LLMs, you can use **LM Studio** desktop application which can be downloaded here: https://lmstudio.ai/

# How to use local LLMs from LM Studio with AutoGen Studio

1. You need to find and open folder `autogenstudio` by running the follow command:
   ```bash
   pip show autogenstudio
   ``` 

2. Open `datamodel.py` file in `autogenstudio` folder, find class `LLMConfig` and change `max_tokens` attribute to a number (such as 4096). The changed class will look like:
    ```python
    @dataclass
    class LLMConfig:
        """Data model for LLM Config for AutoGen"""

        config_list: List[Any] = field(default_factory=list)
        temperature: float = 0
        cache_seed: Optional[Union[int, None]] = None
        timeout: Optional[int] = None
        max_tokens: Optional[int] = 4096
        extra_body: Optional[dict] = None

        def dict(self):
            result = asdict(self)
            result["config_list"] = [c.dict() for c in self.config_list]
            return result
    ```
3. Then host AutoGen Studio web server by run:
    ```bash
    autogenstudio ui --port 8081 --appdir workdir            
    ```
    Then open `http://localhost:8081/` in your browser. Your data will be saved at `workdir` folder.