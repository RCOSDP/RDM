=============================
RDM 実践チュートリアル
=============================

.. toctree::
   :maxdepth: 2
   :caption: 目次

   introduction
   installation
   usage
   metadata_schema
   validation

=============================
1. はじめに
=============================

.. _introduction:

RDM（Research Data Management）オントロジーを活用したメタデータスキーマの設計と実装の方法を解説します。

### 本チュートリアルの目的
本チュートリアルでは、研究データ管理（RDM）におけるメタデータの役割と、RDMオントロジーを活用したメタデータスキーマの構築・利用方法について解説します。研究データの管理・公開・再利用を促進するために、適切なメタデータスキーマの設計と実装は重要な要素となります。

### メタデータとは何か？
メタデータとは、「データについてのデータ」として、研究データの特性や管理情報を記述している情報全般を指します。具体的には、次のような情報が含まれます。

- **識別情報**（タイトル、DOI、作成者）
- **管理情報**（作成日、更新日、バージョン情報）
- **アクセス制御情報**（ライセンス、利用制限）
- **技術情報**（データフォーマット、ファイルサイズ）
- **関連情報**（引用関係、プロジェクトとの関連性）

メタデータを適切に設計・管理することで、研究データの可視性が向上し、再利用が容易になります。

### RDM オントロジーとは？
RDM オントロジーは、研究データのライフサイクル全体（作成、保存、共有、公開、再利用）を体系的に記述するための語彙（ボキャブラリ）を提供するものです。本オントロジーを活用することで、研究データ管理に関わる行為の意味を統一し、異なるシステム間での相互運用性を高めることができます。

### 本チュートリアルの構成
本チュートリアルでは、以下のステップでRDMオントロジーを利用したメタデータスキーマの設計と実装を学びます。

1. **環境構築** - 必要なツールを用いたメタデータスキーマ作成環境のセットアップ
2. **メタデータスキーマの設計** - RDMオントロジーを利用したメタデータスキーマの作成
3. **メタデータの実装と管理** - RDF、JSON-LDフォーマットでの実装
4. **メタデータの検証** - SPARQLクエリやRDFバリデーションを用いたメタデータの品質チェック
5. **メタデータの活用** - 研究データの検索・共有・再利用の方法

このチュートリアルを通じて、RDMオントロジーを用いたメタデータの設計・管理スキルを習得し、実際の研究データ管理に活かしてください。

=============================
2. 環境構築
=============================

.. _installation:

### 必要なツールのインストール

RDM（Research Data Management）オントロジーを活用してメタデータスキーマを設計・実装するには、適切なソフトウェアツールの導入が必要です。以下に、RDMオントロジーを読み込み、マッピングを作成するための主要なソフトウェアを紹介します。

1. **Protégé**（オントロジーの作成・編集）：https://protege.stanford.edu/
2. **RDF4J Workbench**（RDF データの管理・SPARQL クエリ実行）：https://rdf4j.org/documentation/tools/server-workbench/

詳細なインストール手順については、各ツールの公式サイトを参照してください。

=============================
3. 使い方
=============================

.. _usage:

### 1. Protégé を使用した RDM オントロジーのロードと編集

1. Protégé を起動し、「File」→「Open from URL」を選択。
2. `https://github.com/RCOSDP/RDM/tree/main/ontology` にある RDM オントロジーをロード。
3. 「Classes」タブで、定義済みのクラスやプロパティを確認。
4. 扱いたいメタデータスキーマ定義に合わせて、新しいクラスやプロパティを追加。
5. 編集後、「File」→「Save as」で保存。

### 2. RDF4J Workbench を使用した RDM オントロジーのクエリ実行

1. RDF4J Workbench にログイン（`http://localhost:8080/rdf4j-workbench`）。
2. 「Repositories」から新しいリポジトリを作成。
3. RDM オントロジーの RDF ファイルをアップロード。
4. 「SPARQL Query」タブでクエリを実行し、オントロジーのデータを確認。
5. 結果を分析し、適切なマッピングを設計。

=============================
4. メタデータスキーマの設計
=============================

.. _metadata_schema:

### RDM オントロジーを活用したメタデータスキーマ

RDM オントロジーを活用したメタデータ記述の例として、研究データの状態とそのメタデータをモニタリングするデータガバナンス機能に特化したアプリケーションプロファイルであるDG-AP（Data Governance Application Profile）の実装例を紹介します。

.. code-block:: turtle

   @prefix dgap: <https://raw.githubusercontent.com/RCOSDP/RDM/main/ontology/DG-AP/dg_ap.ttl#> .
   @prefix owl: <http://www.w3.org/2002/07/owl#> .
   @prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
   @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
   @prefix rdm: <https://purl.org/rdm/ontology/> .
   @prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

   rdm: a owl:Ontology ;
    rdfs:comment "The Data Governance Application Profile (DG-AP) is an application profile of Research Data Management Ontology (RDM Ontology) specialized to Data Governance application, which can monitor the status of research data and its metadata."@en,
        "データガバナンスアプリケーションプロファイル (DG-AP) は、RDM オントロジーに基づいた、研究データの状態とそのメタデータをモニタリングするデータガバナンス機能に特化したアプリケーションプロファイルです。"@jp ;
    owl:versionInfo "1.0" ;
    owl:imports rdm: .

   dgap:filePath a owl:DatatypeProperty;
      rdfs:label "filePath" ;
      rdfs:comment "File path in Gakunin RDM."@en,
         "Gakunin RDMにおけるファイルパス"@jp ;
   rdfs:domain rdm:Resource ;
   rdfs:range xsd:string ;
   rdfs:subPropertyOf rdm:localIdentifier .

   dgap:runCrate a owl:DatatypeProperty;
      rdfs:label "runCrate" ;
      rdfs:comment "URL of a run-crate file in a project of Gakunin RDM."@en,
         "Gakunin RDM プロジェクト内にある run-crate ファイルの URL"@jp ;
   rdfs:domain rdm:Resource ;
   rdfs:range xsd:string .

   rdm:version rdfs:range xsd:string .

説明:

DG-APでは、RDMオントロジーのクラス定義に準拠しつつ、以下の語彙を新規に定義しています。

- dgap:filePath: DG-AP が扱うアプリケーション（GakuNin RDM）におけるファイルパスを指定しています。
- dgap:runCrate: DG-AP が扱うアプリケーション（GakuNin RDM）内にあるrun-crateファイルのURLを指定しています。

また、RDMオントロジーで定義されている rdm:version の範囲を独自に拡張し、string型で扱っています。
DG-APで定義したメタデータは、JSON-LD形式に変換されウェブアプリケーションで使用されています。詳細はデータガバナンス機能のURL（https://github.com/NII-DG/nii-dg-web）を参照してください。

=============================
5. メタデータの検証
=============================

.. _validation:

### RDF スキーマのバリデーション

メタデータの整合性を確保するために、以下の手順で RDF データの検証を行います。

#### **1. RDF シンタックスの検証**
RDF ファイルの構文が正しいかどうかを確認するために、次のツールを利用できます。

- `W3C RDF Validator <https://www.w3.org/RDF/Validator/>`_
- `Apache Jena riot <https://jena.apache.org/documentation/io/>`_

##### **例: Apache Jena を用いた検証**

```bash
riot --validate RDM_ontology.ttl
```

このコマンドを実行すると、構文エラーがある場合に詳細なエラーメッセージが表示されます。

#### **2. SHACL を用いたスキーマバリデーション**
SHACL（Shapes Constraint Language）を使用すると、RDM オントロジーの構造が適切に定義されているかをチェックできます。

- `TopBraid SHACL Validator <https://www.topquadrant.com/tools/shacl/>`_
- `Apache Jena SHACL Validator <https://jena.apache.org/documentation/shacl/>`_

##### **SHACL 検証の実行**
```bash
shacl validate -datafile RDM_ontology.ttl -shapesfile rdm-shapes.ttl
```

このコマンドにより、RDMオントロジーに準拠しているかが検証され、不適合なデータが報告されます。

#### **3. SPARQL クエリを用いたデータ検証**
SPARQL クエリを利用して、RDMオントロジーのメタデータが特定の基準を満たしているか確認できます。

##### **例: 必須のタイトル情報があるかを確認**
```sparql
PREFIX dcterms: <http://purl.org/dc/terms/>
SELECT ?entity WHERE {
    ?entity a <https://github.com/RCOSDP/RDM/ontology#Entity> .
    FILTER NOT EXISTS { ?entity dcterms:title ?title }
}
```

このクエリを RDF4J Workbench や Apache Jena で実行することで、タイトルがないエンティティを抽出できます。

#### **4. JSON-LD 変換とデータ整合性のチェック**
RDF データは JSON-LD に変換されることがあるため、変換後もデータの整合性を確認する必要があります。

##### **JSON-LD 変換の例（Apache Jena 使用）**
```bash
riot --output=jsonld RDM_ontology.ttl > RDM_ontology.jsonld
```

変換後、JSON-LD の構造を手動で確認するか、`jsonld-cli` などのツールを使用してバリデーションを行います。

#### **5. 自動化のためのスクリプト実装（オプション）**
検証プロセスを自動化するために、Python を用いてバリデーションスクリプトを作成することも可能です。

##### **RDFLib を用いた検証スクリプト（Python）**
```python
from rdflib import Graph

g = Graph()
g.parse("RDM_ontology.ttl", format="turtle")

print("トリプル数:", len(g))
```

このようなスクリプトを活用することで、バリデーションを効率的に実行できます。

---

上記の手法を組み合わせることで、RDMオントロジーの品質を高め、正確なデータ管理を実現できます。
