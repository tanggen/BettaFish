"""
Configuration management module for the Media Engine (pydantic_settings style).
"""

from pathlib import Path
from pydantic_settings import BaseSettings
from pydantic import Field
from typing import Optional, Literal


# 计算 .env 优先级：优先当前工作目录，其次项目根目录
PROJECT_ROOT: Path = Path(__file__).resolve().parents[2]
CWD_ENV: Path = Path.cwd() / ".env"
ENV_FILE: str = str(CWD_ENV if CWD_ENV.exists() else (PROJECT_ROOT / ".env"))

class Settings(BaseSettings):
    """
    全局配置；支持 .env 和环境变量自动加载。
    变量名与原 config.py 大写一致，便于平滑过渡。
    """
    # ====================== 数据库配置 ======================
    DB_HOST: str = Field("rm-wz98aq26ikzp9p751to.mysql.rds.aliyuncs.com", description="数据库主机，例如localhost 或 127.0.0.1。我们也提供云数据库资源便捷配置，日均10w+数据，可免费申请，联系我们：670939375@qq.com NOTE：为进行数据合规性审查与服务升级，云数据库自2025年10月1日起暂停接收新的使用申请")
    DB_PORT: int = Field(3306, description="数据库端口号，默认为3306")
    DB_USER: str = Field("spider", description="数据库用户名")
    DB_PASSWORD: str = Field("&A$PT!n*MWVEd!_5", description="数据库密码")
    DB_NAME: str = Field("media_crawler", description="数据库名称")
    DB_CHARSET: str = Field("utf8mb4", description="数据库字符集，推荐utf8mb4，兼容emoji")
    DB_DIALECT: str = Field("mysql", description="数据库类型，例如 'mysql' 或 'postgresql'。用于支持多种数据库后端（如 SQLAlchemy，请与连接信息共同配置）")

    # ======================= LLM 相关 =======================
    INSIGHT_ENGINE_API_KEY: Optional[str] = Field("sk-EGQq4XL9NuKGuLbWPkM5tv1YSKeHipguVV8HesnuFca3bpSc",
                                                  description="Insight Agent（推荐 kimi-k2，官方申请地址：https://platform.moonshot.cn/）API 密钥，用于主 LLM。🚩请先按推荐配置申请并跑通，再根据需要调整 KEY、BASE_URL 与 MODEL_NAME。")
    INSIGHT_ENGINE_BASE_URL: Optional[str] = Field("https://api.moonshot.cn/v1",
                                                   description="Insight Agent LLM BaseUrl，可根据厂商自定义")
    INSIGHT_ENGINE_MODEL_NAME: str = Field("kimi-k2-0711-preview",
                                           description="Insight Agent LLM 模型名称，例如 kimi-k2-0711-preview")

    MEDIA_ENGINE_API_KEY: Optional[str] = Field("sk-EGQq4XL9NuKGuLbWPkM5tv1YSKeHipguVV8HesnuFca3bpSc",
                                                description="Insight Agent（推荐 kimi-k2，官方申请地址：https://platform.moonshot.cn/）API 密钥，用于主 LLM。🚩请先按推荐配置申请并跑通，再根据需要调整 KEY、BASE_URL 与 MODEL_NAME。")
    MEDIA_ENGINE_BASE_URL: Optional[str] = Field("https://api.moonshot.cn/v1",
                                                 description="Insight Agent LLM BaseUrl，可根据厂商自定义")
    MEDIA_ENGINE_MODEL_NAME: str = Field("kimi-k2-0711-preview",
                                         description="Insight Agent LLM 模型名称，例如 kimi-k2-0711-preview")

    SEARCH_TIMEOUT: int = Field(240, description="搜索超时（秒）")
    SEARCH_CONTENT_MAX_LENGTH: int = Field(20000, description="用于提示的最长内容长度")
    MAX_REFLECTIONS: int = Field(2, description="最大反思轮数")
    MAX_PARAGRAPHS: int = Field(5, description="最大段落数")

    MINDSPIDER_API_KEY: Optional[str] = Field("sk-a30d9ed6ab4545889655de0d0dccf529",
                                              description="MindSpider Agent（推荐 deepseek，官方申请地址：https://platform.deepseek.com/）API 密钥")
    MINDSPIDER_BASE_URL: Optional[str] = Field("https://api.deepseek.com",
                                               description="MindSpider Agent BaseUrl，可按所选服务配置")
    MINDSPIDER_MODEL_NAME: Optional[str] = Field("deepseek-chat",
                                                 description="MindSpider Agent 模型名称，例如 deepseek-reasoner")
    
    OUTPUT_DIR: str = Field("reports", description="输出目录")
    SAVE_INTERMEDIATE_STATES: bool = Field(True, description="是否保存中间状态")


    QUERY_ENGINE_API_KEY: Optional[str] = Field("sk-a30d9ed6ab4545889655de0d0dccf529", description="Query Agent（推荐 deepseek，官方申请地址：https://platform.deepseek.com/）API 密钥")
    QUERY_ENGINE_BASE_URL: Optional[str] = Field("https://api.deepseek.com", description="Query Agent LLM BaseUrl")
    QUERY_ENGINE_MODEL_NAME: str = Field("deepseek-reasoner", description="Query Agent LLM 模型名称，如 deepseek-reasoner")

    REPORT_ENGINE_API_KEY: Optional[str] = Field("sk-Jj3G9NHGphN5a4983768D9443568469aBe1702A4E906140a",
                                                 description="Report Agent（推荐 gemini-2.5-pro，中转厂商申请地址：https://aihubmix.com/?aff=8Ds9）API 密钥")
    REPORT_ENGINE_BASE_URL: Optional[str] = Field("https://aihubmix.com/v1",
                                                  description="Report Agent LLM BaseUrl，可根据中转服务调整")
    REPORT_ENGINE_MODEL_NAME: str = Field("gemini-2.5-pro", description="Report Agent LLM 模型名称，如 gemini-2.5-pro")

    FORUM_HOST_API_KEY: Optional[str] = Field("sk-96985a31fd1f470baa5833e7945e73fc",
                                              description="Forum Host（推荐 qwen-plus，官方申请地址：https://www.aliyun.com/product/bailian）API 密钥")
    FORUM_HOST_BASE_URL: Optional[str] = Field("https://dashscope.aliyuncs.com/compatible-mode/v1",
                                               description="Forum Host LLM BaseUrl，可按所选服务配置")
    FORUM_HOST_MODEL_NAME: Optional[str] = Field("qwen-plus", description="Forum Host LLM 模型名称，例如 qwen-plus")
    
    KEYWORD_OPTIMIZER_API_KEY: str = Field("sk-96985a31fd1f470baa5833e7945e73fc", description="SQL keyword Optimizer（小参数Qwen3模型，这里我使用了硅基流动这个平台，申请地址：https://cloud.siliconflow.cn/）API密钥")
    KEYWORD_OPTIMIZER_BASE_URL: Optional[str] = Field("https://dashscope.aliyuncs.com/compatible-mode/v1", description="Keyword Optimizer BaseUrl")
    KEYWORD_OPTIMIZER_MODEL_NAME: str = Field("Qwen/Qwen3-30B-A3B-Instruct-2507", description="Keyword Optimizer LLM模型名称，如Qwen/Qwen3-30B-A3B-Instruct-2507")

    # ================== 网络工具配置 ====================
    TAVILY_API_KEY: str = Field("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", description="Tavily API（申请地址：https://www.tavily.com/）API密钥，用于Tavily网络搜索")
    
    SEARCH_TOOL_TYPE: Literal["AnspireAPI", "BochaAPI"] = Field("BochaAPI", description="网络搜索工具类型，支持BochaAPI或AnspireAPI两种，默认为AnspireAPI")
    BOCHA_BASE_URL: Optional[str] = Field("https://api.bocha.cn/v1/web-search",
                                          description="Bocha AI 搜索BaseUrl或博查网页搜索BaseUrl")
    BOCHA_WEB_SEARCH_API_KEY: Optional[str] = Field("sk-64d9e5784a2d47d097aa3620886ef35d",
                                                    description="Bocha API（申请地址：https://open.bochaai.com/）API密钥，用于Bocha搜索")
    # Anspire AI Search API（申请地址：https://open.anspire.cn/）
    ANSPIRE_BASE_URL: Optional[str] = Field("https://plugin.anspire.cn/api/ntsearch/search", description="Anspire AI 搜索BaseUrl")
    ANSPIRE_API_KEY: Optional[str] = Field(None, description="Anspire AI Search API（申请地址：https://open.anspire.cn/）API密钥，用于Anspire搜索")

    class Config:
        env_file = ENV_FILE
        env_prefix = ""
        case_sensitive = False
        extra = "allow"


settings = Settings()
