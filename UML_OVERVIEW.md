# Version UML textuelle standard, compatible avec PlantUML pour possible utilisation ultérieure

@startuml
title Architecture UML — quant_system

package "data" {
    class DataLoader {
        +load(path)
        +validate()
    }

    class Preprocessor {
        +clean(data)
        +normalize(data)
    }
}

package "indicators" {
    class EMA {
        +compute(series, period)
    }

    class ADX {
        +compute(data)
    }

    class Volatility {
        +compute(data)
    }
}

package "structure" {
    class SwingDetector {
        +detect(data)
    }

    class ZigZag {
        +compute(data, threshold)
    }
}

package "orderflow" {
    class Delta {
        +compute(data)
    }

    class Imbalance {
        +compute(data)
    }

    class Absorption {
        +compute(data)
    }
}

package "features" {
    class FeatureBuilder {
        +build(data, indicators, structure, orderflow)
    }

    class Encoders {
        +encode(data)
    }
}

package "signals" {
    class SignalEngine {
        +generate(features)
    }

    class Scoring {
        +score(signals)
    }
}

package "optimization" {
    class ParameterSearch {
        +optimize(config)
    }
}

package "attribution" {
    class AttributionEngine {
        +attribute(signals)
    }
}

package "utils" {
    class Hashing {
        +compute_hash(obj)
    }

    class Helpers {
        +log()
        +timer()
    }
}

package "pipeline" {
    class Pipeline {
        +run_pipeline(data_path, config_path)
    }
}

' Relations
Pipeline --> DataLoader
Pipeline --> Preprocessor
Pipeline --> EMA
Pipeline --> ADX
Pipeline --> Volatility
Pipeline --> SwingDetector
Pipeline --> ZigZag
Pipeline --> Delta
Pipeline --> Imbalance
Pipeline --> Absorption
Pipeline --> FeatureBuilder
Pipeline --> SignalEngine
Pipeline --> Scoring
Pipeline --> AttributionEngine
Pipeline --> Hashing

@enduml
