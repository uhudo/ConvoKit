from setuptools import setup

setup(
    name="convokit",
    author="Jonathan P. Chang, Caleb Chiam, Liye Fu, Andrew Wang, Justine Zhang, Cristian Danescu-Niculescu-Mizil",
    author_email="cristian@cs.cornell.edu",
    url="https://github.com/CornellNLP/ConvoKit",
    description="ConvoKit",
    version="2.5.3",
    packages=[
        "convokit",
        "convokit.bag_of_words",
        "convokit.classifier",
        "convokit.coordination",
        "convokit.fighting_words",
        "convokit.forecaster",
        "convokit.forecaster.CRAFT",
        "convokit.hyperconvo",
        "convokit.model",
        "convokit.paired_prediction",
        "convokit.phrasing_motifs",
        "convokit.politeness_collections",
        "convokit.politeness_collections.politeness_api",
        "convokit.politeness_collections.politeness_api.features",
        "convokit.politeness_collections.politeness_local",
        "convokit.politeness_collections.politeness_cscw_zh",
        "convokit.politenessStrategies",
        "convokit.prompt_types",
        "convokit.ranker",
        "convokit.text_processing",
        "convokit.speaker_convo_helpers",
        "convokit.speakerConvoDiversity",
        "convokit.expected_context_framework",
        "convokit.surprise",
    ],
    package_data={
        "convokit": [
            "data/*.txt",
            "politeness_collections/politeness_local/lexicons/*.json",
            "politeness_collections/politeness_cscw_zh/lexicons/*.json",
        ]
    },
    install_requires=[
        "matplotlib>=3.0.0",
        "pandas>=0.23.4",
        "msgpack-numpy>=0.4.3.2",
        "spacy>=2.3.5",
        "scipy>=1.1.0",
        "scikit-learn>=0.20.0",
        "nltk>=3.4",
        "dill>=0.2.9",
        "joblib>=0.13.2",
        "clean-text>=0.1.1",
        "unidecode>=1.1.1",
    ],
    extras_require={
        "craft": ["torch>=0.12"],
    },
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
