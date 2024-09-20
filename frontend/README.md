# Usage Guidelines

There is two domain models of RDM Ontology; focused on Resource and focused on Activity. The former is focused on describing Resource as a outcome of research activities. The latter is focused on research activities itself. These two can be linked by using rdm property, however, it is not recommended because of the complexity.

## Domain Model Focused on Resource

![Resource domain model](../docs/domain_model_Resource.png)

To describe research outcomes such as research data, the main entity should be of type Resource. (It is recommended that a subclass of Resource be selected and used according to the category of research outcomes.) Related entities such as research project can be described by linking to the main entity. Activity entities is not recommended to add to this style of describing to divide the result of research activity (Resource) and the process (Activity).
Examples of Resource focused description is in two formats:

- [JSON-LD](../example/example_research_data.json)
- [turtle](../example/example_research_data.ttl)

## Domain Model Focused on Activity

![Resource domain model](../docs/domain_model_Activity.png)

To describe research activities as a log, the main entity should be a subclass of Activity class. Resource entities can be linked as a result, a target and a used tool of the activity. Linking other entities to Resource is not recommended when the main entity is subclass of Activity, as well as Resourced focused case.

# Term Definitions Overview

| prefix | Namespace                                   |
| ------ | ------------------------------------------- |
| rdm    | https://purl.org/rdm/ontology/              |
| owl    | http://www.w3.org/2002/07/owl#              |
| rdf    | http://www.w3.org/1999/02/22-rdf-syntax-ns# |
| rdfs   | http://www.w3.org/2000/01/rdf-schema#       |
| xsd    | http://www.w3.org/2001/XMLSchema#           |

## Class

### Base Class

| Class         | Activity                               |
| ------------- | -------------------------------------- |
| IRI           | https://purl.org/rdm/ontology/Activity |
| definition@en | An action or activity.                 |
| definition@en | 行動や行為                             |

| Class         | Actor                                                       |
| ------------- | ----------------------------------------------------------- |
| IRI           | https://purl.org/rdm/ontology/Actor                         |
| definition@en | Person or organization that is the subject of the Activity. |
| definition@en | Activity を行う主語にあたる人または組織                     |

| Class         | Object                                              |
| ------------- | --------------------------------------------------- |
| IRI           | https://purl.org/rdm/ontology/Object                |
| definition@en | Things and objects that are the object of Activity. |
| definition@en | Activity の目的語となる事物                         |

<!-- The following is generated automatically -->

### Activity

| Class         | Accept                                   |
|---------------|------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Accept     |
| definition@en | An act of approving Resource or request. |
| definition@ja | Resource や依頼を承認する行動                      |
| subClassOf    | rdm:Activity                             |

| Class         | Align                                 |
|---------------|---------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Align   |
| definition@en | An act of editing Resource to format. |
| definition@ja | Resource をフォーマットに合わせて編集する行動           |
| subClassOf    | rdm:Activity                          |

| Class         | Anonymize                               |
|---------------|-----------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Anonymize |
| definition@en | An act of making Resource anonymous.    |
| definition@ja | Resource を匿名化する行動                       |
| subClassOf    | rdm:Activity                            |

| Class         | Ask                                                |
|---------------|----------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Ask                  |
| definition@en | An act of asking questions to Person, chatbot etc. |
| definition@ja | Person やチャットボットなどに質問をする行動                          |
| subClassOf    | rdm:Activity                                       |

| Class         | Assign                                |
|---------------|---------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Assign  |
| definition@en | An act of assigning a role to Person. |
| definition@ja | Person に役割を任命する行動                     |
| subClassOf    | rdm:Activity                          |

| Class         | Authorize                                            |
|---------------|------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Authorize              |
| definition@en | An act of granting permission or right to an object. |
| definition@ja | 権利や許可を与える行動                                          |
| subClassOf    | rdm:Activity                                         |

| Class         | Check                                                                     |
|---------------|---------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Check                                       |
| definition@en | An act of checking the regulation for Resource, such as using checkboxes. |
| definition@ja | チェックボックスに印をつけるなど、規定の項目に関して確認する行動                                          |
| subClassOf    | rdm:Activity                                                              |

| Class         | Cleanse                                          |
|---------------|--------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Cleanse            |
| definition@en | An act of performing data cleansing of Resource. |
| definition@ja | Resource をデータクレンジングする行動                          |
| subClassOf    | rdm:Activity                                     |

| Class         | Collect                               |
|---------------|---------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Collect |
| definition@en | An act of collecting Resource.        |
| definition@ja | Resource を収集する行動                      |
| subClassOf    | rdm:Activity                          |

| Class         | Comment                                     |
|---------------|---------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Comment       |
| definition@en | An act of generating a comment on Resource. |
| definition@ja | Resource に対してコメントをする行動                      |
| subClassOf    | rdm:Activity                                |

| Class         | Connect                                          |
|---------------|--------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Connect            |
| definition@en | An act of connecting service to another service. |
| definition@ja | サービスを別のサービスに接続する行動                               |
| subClassOf    | rdm:Activity                                     |

| Class         | Convert                                            |
|---------------|----------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Convert              |
| definition@en | An act of converting Resource into a new Resource. |
| definition@ja | Resource を新たな Resource に変換する行動                     |
| subClassOf    | rdm:Activity                                       |

| Class         | Create                                                                     |
|---------------|----------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Create                                       |
| definition@en | An act of creating/producing/generating Resource, Project, Collection etc. |
| definition@ja | Project, Resource, Collection などを作成する行動                                    |
| subClassOf    | rdm:Activity                                                               |

| Class         | Dump                                      |
|---------------|-------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Dump        |
| definition@en | An act of creating a log file by dumping. |
| definition@ja | ダンプによりログファイルを作成する行動                       |
| subClassOf    | rdm:Create                                |

| Class         | Deploy                                               |
|---------------|------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Deploy                 |
| definition@en | An act of deploying SoftwareApplication or Resource. |
| definition@ja | Resource, SoftwareApplicationをデプロイする行動               |
| subClassOf    | rdm:Activity                                         |

| Class         | Develop                               |
|---------------|---------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Develop |
| definition@en | An act of developing a program.       |
| definition@ja | プログラミングで実装する行動                        |
| subClassOf    | rdm:Activity                          |

| Class         | Download                               |
|---------------|----------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Download |
| definition@en | An act of downloading Resource.        |
| definition@ja | Resource をダウンロードする行動                   |
| subClassOf    | rdm:Activity                           |

| Class         | Evaluate                                            |
|---------------|-----------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Evaluate              |
| definition@en | An act of evaluating Resource, such as peer-review. |
| definition@ja | ピアレビューなど、Resource を評価する行動                           |
| subClassOf    | rdm:Activity                                        |

| Class         | Execute                                                         |
|---------------|-----------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Execute                           |
| definition@en | An act of executing SoftwareApplication, Resource, program etc. |
| definition@ja | Resource, SoftwareApplication, プログラムを実行する行動                     |
| subClassOf    | rdm:Activity                                                    |

| Class         | Get                                                    |
|---------------|--------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Get                      |
| definition@en | An act of getting/obtaining Resource, information etc. |
| definition@ja | Resource または情報などを取得する行動                                |
| subClassOf    | rdm:Activity                                           |

| Class         | Inform                                                 |
|---------------|--------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Inform                   |
| definition@en | An act of notifying Person/Institution of information. |
| definition@ja | Person, Institution に対して通知する行動                         |
| subClassOf    | rdm:Activity                                           |

| Class         | Ingest                                                                                              |
|---------------|-----------------------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Ingest                                                                |
| definition@en | An act of getting and adding metadata to Resource from public information as part of data curation. |
| definition@ja | キュレーションの一環として、Resource のメタデータを外部から取得し付与する行動                                                         |
| subClassOf    | rdm:Activity                                                                                        |

| Class         | Integrate                                                                   |
|---------------|-----------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Integrate                                     |
| definition@en | An act of integrating different forms of metadata as part of data curation. |
| definition@ja | キュレーションの一環として、メタデータを統合する行動                                                  |
| subClassOf    | rdm:Activity                                                                |

| Class         | Preserve                                                                      |
|---------------|-------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Preserve                                        |
| definition@en | An act of saving and storing Resource to Repository, SoftwareApplication etc. |
| definition@ja | Resource を Repository, SoftwareApplication などに保存・保管する行動                       |
| subClassOf    | rdm:Activity                                                                  |

| Class         | Archive                               |
|---------------|---------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Archive |
| definition@en | An act of archiving Resource.         |
| definition@ja | Resource をアーカイブする行動                   |
| subClassOf    | rdm:Preserve                          |

| Class         | Publish                                                                                                                                |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Publish                                                                                                  |
| definition@en | An act of making Resource public, such as by pushing "publish" button on publishing service. (including Resource of any access rights) |
| definition@ja | 公開ボタンを押すなどして、Resource を公開する行動(アクセス権の種類は問わない)                                                                                           |
| subClassOf    | rdm:Activity                                                                                                                           |

| Class         | Register                                                                            |
|---------------|-------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Register                                              |
| definition@en | An act of registering Resource to Repository, SoftwareApplication or other service. |
| definition@ja | Repository, SoftwareApplication もしくはその他サービスに、 Resource を登録する行動                      |
| subClassOf    | rdm:Activity                                                                        |

| Class         | Reject                                                             |
|---------------|--------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Reject                               |
| definition@en | An act of rejecting proposal/assigned role/submitted Resource etc. |
| definition@ja | 提出された Resource や提案、割り当てられた役割などを取り下げる行動                             |
| subClassOf    | rdm:Activity                                                       |

| Class         | Rename                               |
|---------------|--------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Rename |
| definition@en | An act of renaming Resource.         |
| definition@ja | Resource の名称を変更する行動                  |
| subClassOf    | rdm:Activity                         |

| Class         | Reorganize                                      |
|---------------|-------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Reorganize        |
| definition@en | An act of changing folder structure of Dataset. |
| definition@ja | Dataset のフォルダ構成を変更する行動                          |
| subClassOf    | rdm:Activity                                    |

| Class         | Restructure                                                                          |
|---------------|--------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Restructure                                            |
| definition@en | An act of re-structuring Resource as part of data curation, such as sorting a table. |
| definition@ja | 表データをソートするなど、キュレーションの一環として Resource を再構成する行動                                         |
| subClassOf    | rdm:Activity                                                                         |

| Class         | Schedule                               |
|---------------|----------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Schedule |
| definition@en | An act of scheduling future Event.     |
| definition@ja | 未来に行われる Event を設定する行動                  |
| subClassOf    | rdm:Activity                           |

| Class         | Search                                                            |
|---------------|-------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Search                              |
| definition@en | An act of searching Resource, such as by pushing "search" button. |
| definition@ja | 検索ボタンの押下など、Resource を検索する行動                                       |
| subClassOf    | rdm:Activity                                                      |

| Class         | Select                               |
|---------------|--------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Select |
| definition@en | An act of selecting from options.    |
| definition@ja | 選択肢の中から利用するものを選択する行動                 |
| subClassOf    | rdm:Activity                         |

| Class         | Send                               |
|---------------|------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Send |
| definition@en | An act of dispatching Resource.    |
| definition@ja | Resource を送る行動                     |
| subClassOf    | rdm:Activity                       |

| Class         | Suggest                                    |
|---------------|--------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Suggest      |
| definition@en | An act of presenting or proposing options. |
| definition@ja | 選択肢を提示する行動                                 |
| subClassOf    | rdm:Activity                               |

| Class         | Update                                                |
|---------------|-------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Update                  |
| definition@en | An act of updating an existing Resource with changes. |
| definition@ja | 既存の Resource に変更を加え更新する行動                             |
| subClassOf    | rdm:Activity                                          |

| Class         | Upload                                                               |
|---------------|----------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Upload                                 |
| definition@en | An act of uploading Resource to Repository, SoftwareApplication etc. |
| definition@ja | Resource を SoftwareApplicationやRepository 等にアップロードする行動               |
| subClassOf    | rdm:Activity                                                         |

| Class         | Visualize                                                                 |
|---------------|---------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Visualize                                   |
| definition@en | An act of creating a visualization based on data, such as making a graph. |
| definition@ja | グラフを生成するなど、データを元に可視化する行動                                                  |
| subClassOf    | rdm:Activity                                                              |

### Actor

| Class         | Institution                               |
|---------------|-------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Institution |
| definition@en | An organization.                          |
| definition@ja | 機関や組織                                     |
| subClassOf    | rdm:Actor                                 |

| Class         | FundingAgency                                   |
|---------------|-------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/FundingAgency     |
| definition@en | An organization that funds research activities. |
| definition@ja | 研究資金提供機関                                        |
| subClassOf    | rdm:Institution                                 |

| Class         | Person                               |
|---------------|--------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Person |
| definition@en | A person.                            |
| definition@ja | 人物                                   |
| subClassOf    | rdm:Actor                            |

### Object

| Class         | Collection                               |
|---------------|------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Collection |
| definition@en | A collection of items.                   |
| definition@ja | オブジェクトのコレクション                            |
| subClassOf    | rdm:Object                               |

| Class         | DataManagementPlan                               |
|---------------|--------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/DataManagementPlan |
| definition@en | A data management plan (DMP).                    |
| definition@ja | データ管理計画(DMP)                                     |
| subClassOf    | rdm:Object                                       |

| Class         | Event                               |
|---------------|-------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Event |
| definition@en | An event, such as conferences etc.  |
| definition@ja | 学会など、イベントや催し物                       |
| subClassOf    | rdm:Object                          |

| Class         | Experiment                               |
|---------------|------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Experiment |
| definition@en | Experiment                               |
| definition@ja | 実験                                       |
| subClassOf    | rdm:Object                               |

| Class         | Grant                               |
|---------------|-------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Grant |
| definition@en | A grant for research activities.    |
| definition@ja | 研究資金プログラム                           |
| subClassOf    | rdm:Object                          |

| Class         | Identifier                               |
|---------------|------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Identifier |
| definition@en | An identifier.                           |
| definition@ja | 識別子                                      |
| subClassOf    | rdm:Object                               |

| Class         | Intangible                                    |
|---------------|-----------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Intangible      |
| definition@en | Abstract class for concepts without entities. |
| definition@ja | 実体を伴わない概念のための抽象クラス                            |
| subClassOf    | rdm:Object                                    |

| Class         | Role                               |
|---------------|------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Role |
| definition@en | Roles and positions.               |
| definition@ja | 役割、役職                              |
| subClassOf    | rdm:Intangible                     |

| Class         | Project                               |
|---------------|---------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Project |
| definition@en | A research project.                   |
| definition@ja | 研究プロジェクト                              |
| subClassOf    | rdm:Object                            |

| Class         | Repository                               |
|---------------|------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Repository |
| definition@en | A repository.                            |
| definition@ja | リポジトリ                                    |
| subClassOf    | rdm:Object                               |

| Class         | Resource                                                           |
|---------------|--------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Resource                             |
| definition@en | A digital object, such as research data, video of experiments rtc. |
| definition@ja | 研究データや実験動画など、デジタルオブジェクト                                            |
| subClassOf    | rdm:Object                                                         |

| Class         | Audio                               |
|---------------|-------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Audio |
| definition@en | An audio file.                      |
| definition@ja | 音声                                  |
| subClassOf    | rdm:Resource                        |

| Class         | Book                               |
|---------------|------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Book |
| definition@en | A book.                            |
| definition@ja | 書籍                                 |
| subClassOf    | rdm:Resource                       |

| Class         | ConferenceObject                               |
|---------------|------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/ConferenceObject |
| definition@en | A Resource related to conferences.             |
| definition@ja | カンファレンスに関連するリソース                               |
| subClassOf    | rdm:Resource                                   |

| Class         | ConferencePaper                               |
|---------------|-----------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/ConferencePaper |
| definition@en | A conference paper.                           |
| definition@ja | カンファレンスペーパー                                   |
| subClassOf    | rdm:Resource                                  |

| Class         | ConferenceProceeding                               |
|---------------|----------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/ConferenceProceeding |
| definition@en | A conference proceeding.                           |
| definition@ja | カンファレンスプロシーディング                                    |
| subClassOf    | rdm:Resource                                       |

| Class         | Dataset                               |
|---------------|---------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Dataset |
| definition@en | A dataset.                            |
| definition@ja | データセット                                |
| subClassOf    | rdm:Resource                          |

| Class         | EducationalResource                                            |
|---------------|----------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/EducationalResource              |
| definition@en | A Resource related to educational, such as slides for lecture. |
| definition@ja | 教育関連資料                                                         |
| subClassOf    | rdm:Resource                                                   |

| Class         | Image                               |
|---------------|-------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Image |
| definition@en | An image file.                      |
| definition@ja | 画像                                  |
| subClassOf    | rdm:Resource                        |

| Class         | Journal                               |
|---------------|---------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Journal |
| definition@en | A journal.                            |
| definition@ja | ジャーナル                                 |
| subClassOf    | rdm:Resource                          |

| Class         | JournalArticle                               |
|---------------|----------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/JournalArticle |
| definition@en | An article published in a journal.           |
| definition@ja | ジャーナル論文                                      |
| subClassOf    | rdm:Resource                                 |

| Class         | Message                               |
|---------------|---------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Message |
| definition@en | Message and comment.                  |
| definition@ja | メッセージやコメント                            |
| subClassOf    | rdm:Resource                          |

| Class         | MetadataDocument                               |
|---------------|------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/MetadataDocument |
| definition@en | Metadata of any Resource.                      |
| definition@ja | Resource に関するメタデータ                             |
| subClassOf    | rdm:Resource                                   |

| Class         | OtherResource                               |
|---------------|---------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/OtherResource |
| definition@en | An other Resource.                          |
| definition@ja | その他のリソース                                    |
| subClassOf    | rdm:Resource                                |

| Class         | Preprint                               |
|---------------|----------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Preprint |
| definition@en | A preprint.                            |
| definition@ja | プレプリント                                 |
| subClassOf    | rdm:Resource                           |

| Class         | Report                               |
|---------------|--------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Report |
| definition@en | A report.                            |
| definition@ja | レポート、報告書                             |
| subClassOf    | rdm:Resource                         |

| Class         | Review                               |
|---------------|--------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Review |
| definition@en | Review documents and evaluations.    |
| definition@ja | レビュー文書や評価                            |
| subClassOf    | rdm:Resource                         |

| Class         | Standard                               |
|---------------|----------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Standard |
| definition@en | A standard.                            |
| definition@ja | 標準                                     |
| subClassOf    | rdm:Resource                           |

| Class         | Thesis                               |
|---------------|--------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Thesis |
| definition@en | A thesis.                            |
| definition@ja | 学位論文                                 |
| subClassOf    | rdm:Resource                         |

| Class         | Video                               |
|---------------|-------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Video |
| definition@en | A video file.                       |
| definition@ja | 動画                                  |
| subClassOf    | rdm:Resource                        |

| Class         | Workflow                               |
|---------------|----------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Workflow |
| definition@en | A workflow.                            |
| definition@ja | ワークフロー                                 |
| subClassOf    | rdm:Resource                           |

| Class         | RightsStatement                                     |
|---------------|-----------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/RightsStatement       |
| definition@en | A higer-level class that relates to various rights. |
| definition@ja | 権利関係全般に関連するクラス                                      |
| subClassOf    | rdm:Object                                          |

| Class         | AccessRights                               |
|---------------|--------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/AccessRights |
| definition@en | An access right o Resource.                |
| definition@ja | リソースへのアクセス権                                |
| subClassOf    | rdm:RightsStatement                        |

| Class         | License                               |
|---------------|---------------------------------------|
| IRI           | https://purl.org/rdm/ontology/License |
| definition@en | A license of Resource.                |
| definition@ja | リソースのライセンス                            |
| subClassOf    | rdm:RightsStatement                   |

| Class         | SoftwareApplication                               |
|---------------|---------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/SoftwareApplication |
| definition@en | A software application.                           |
| definition@ja | ソフトウェアアプリケーション                                    |
| subClassOf    | rdm:Object                                        |
## Property

### Datatype Property

| Property      | additionalName                                       |
|---------------|------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/additionalName         |
| domain        | rdm:Person                                           |
| definition@en | An additional name for this Person e.g. middle name. |
| definition@ja | ミドルネームなど、その他の名前                                      |

| Property      | address                               |
|---------------|---------------------------------------|
| IRI           | https://purl.org/rdm/ontology/address |
| domain        | rdm:Institution                       |
| range         | xsd:string                            |
| definition@en | Address of this Institution.          |
| definition@ja | 研究機関の住所                               |

| Property      | approximateSize                                                               |
|---------------|-------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/approximateSize                                 |
| domain        | rdm:DataManagementPlan                                                        |
| range         | xsd:string                                                                    |
| definition@en | Approximate size of research data to be described in this DataManagementPlan. |
| definition@ja | DMPにおける概略データ量                                                                 |

| Property      | collectionSize                               |
|---------------|----------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/collectionSize |
| domain        | rdm:Collection                               |
| range         | xsd:nonNegativeInteger                       |
| definition@en | The number of items in this Collection.      |
| definition@ja | 所定のパッケージに含まれるデータセットの総数                       |

| Property      | contact                                                                                             |
|---------------|-----------------------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/contact                                                               |
| domain        | rdm:DataManagementPlan                                                                              |
| range         | xsd:string                                                                                          |
| definition@en | Contacts for data management organizations and managers to be described in this DataManagementPlan. |
| definition@ja | DMPにおけるデータ管理機関・管理者への連絡先                                                                             |

| Property      | copyright                               |
|---------------|-----------------------------------------|
| IRI           | https://purl.org/rdm/ontology/copyright |
| domain        | rdm:License                             |
| range         | xsd:string                              |
| definition@en | A copyright notice.                     |
| definition@ja | コピーライト表記                                |

| Property      | dataAccessRequirements                                                     |
|---------------|----------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/dataAccessRequirements                       |
| domain        | rdm:AccessRights                                                           |
| range         | xsd:string                                                                 |
| definition@en | Conditions and method of access to the Resource under access restrictions. |
| definition@ja | アクセス権が限定公開の場合のアクセス条件と方法                                                    |

| Property      | dataDescription                                                              |
|---------------|------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/dataDescription                                |
| domain        | rdm:DataManagementPlan                                                       |
| definition@ja | DMPにおけるデータの説明                                                                |
| definition@en | The description of research data to be described in this DataManagementPlan. |

| Property      | dataEncodingFormat                                                      |
|---------------|-------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/dataEncodingFormat                        |
| domain        | rdm:DataManagementPlan                                                  |
| definition@ja | DMPで記述した研究データのフォーマット                                                    |
| definition@en | The format of research data to be described in this DataManagementPlan. |

| Property      | dataNumber                                           |
|---------------|------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/dataNumber             |
| domain        | rdm:DataManagementPlan                               |
| range         | xsd:nonNegativeInteger                               |
| definition@ja | DMPにおけるデータNo.                                        |
| definition@en | The data number assigned to this DataManagementPlan. |

| Property      | date                               |
|---------------|------------------------------------|
| IRI           | https://purl.org/rdm/ontology/date |
| range         | xsd:date ,xsd:dateTime             |
| definition@en | A date or datetime.                |
| definition@ja | 日付または日時                            |

| Property      | dateAvailable                                                                       |
|---------------|-------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/dateAvailable                                         |
| subPropertyOf | rdm:date                                                                            |
| domain        | rdm:AccessRights                                                                    |
| definition@en | Scheduled date of open access of the Resource under the rights of embargoed access. |
| definition@ja | 公開猶予の場合の公開予定日                                                                       |

| Property      | dateCreated                                  |
|---------------|----------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/dateCreated    |
| subPropertyOf | rdm:date                                     |
| domain        | rdm:Resource                                 |
| definition@en | The date on which this Resource was created. |
| definition@ja | リソースの作成日                                     |

| Property      | dateEnded                                      |
|---------------|------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/dateEnded        |
| subPropertyOf | rdm:date                                       |
| domain        | rdm:Activity ,rdm:Event ,rdm:Project ,rdm:Role |
| definition@en | The end date of this Class.                    |
| definition@ja | クラスの終了日                                        |

| Property      | dateModified                                               |
|---------------|------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/dateModified                 |
| subPropertyOf | rdm:date                                                   |
| domain        | rdm:Resource                                               |
| definition@en | The date on which the Resource was most recently modified. |
| definition@ja | リソースの最終更新日                                                 |

| Property      | datePublished                                  |
|---------------|------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/datePublished    |
| subPropertyOf | rdm:date                                       |
| domain        | rdm:Resource                                   |
| definition@en | The date on which this Resource was published. |
| definition@ja | リソースの発行日・公開日                                   |

| Property      | dateStarted                                    |
|---------------|------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/dateStarted      |
| subPropertyOf | rdm:date                                       |
| domain        | rdm:Activity ,rdm:Event ,rdm:Project ,rdm:Role |
| definition@en | The start date of this Class.                  |
| definition@ja | クラスの開始日                                        |

| Property      | dateUpdated                                                         |
|---------------|---------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/dateUpdated                           |
| subPropertyOf | rdm:date                                                            |
| domain        | rdm:Event                                                           |
| definition@en | The date on which this Event information was most recently updated. |
| definition@ja | イベントの内容更新日                                                          |

| Property      | sdDatePublished                               |
|---------------|-----------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/sdDatePublished |
| subPropertyOf | rdm:date                                      |
| domain        | rdm:Resource                                  |
| definition@en | The acquisition date of this Resource.        |
| definition@ja | 外部ファイルの取得日                                    |

| Property      | dateAvailable                                                                       |
|---------------|-------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/dateAvailable                                         |
| domain        | rdm:AccessRights                                                                    |
| definition@en | Scheduled date of open access of the Resource under the rights of embargoed access. |
| definition@ja | 公開猶予の場合の公開予定日                                                                       |

| Property      | dateCreated                                  |
|---------------|----------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/dateCreated    |
| domain        | rdm:Resource                                 |
| definition@en | The date on which this Resource was created. |
| definition@ja | リソースの作成日                                     |

| Property      | dateEnded                                      |
|---------------|------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/dateEnded        |
| domain        | rdm:Activity ,rdm:Event ,rdm:Project ,rdm:Role |
| definition@en | The end date of this Class.                    |
| definition@ja | クラスの終了日                                        |

| Property      | dateModified                                               |
|---------------|------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/dateModified                 |
| domain        | rdm:Resource                                               |
| definition@en | The date on which the Resource was most recently modified. |
| definition@ja | リソースの最終更新日                                                 |

| Property      | datePublished                                  |
|---------------|------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/datePublished    |
| domain        | rdm:Resource                                   |
| definition@en | The date on which this Resource was published. |
| definition@ja | リソースの発行日・公開日                                   |

| Property      | dateStarted                                    |
|---------------|------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/dateStarted      |
| domain        | rdm:Activity ,rdm:Event ,rdm:Project ,rdm:Role |
| definition@en | The start date of this Class.                  |
| definition@ja | クラスの開始日                                        |

| Property      | dateUpdated                                                         |
|---------------|---------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/dateUpdated                           |
| domain        | rdm:Event                                                           |
| definition@en | The date on which this Event information was most recently updated. |
| definition@ja | イベントの内容更新日                                                          |

| Property      | description                                                                    |
|---------------|--------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/description                                      |
| domain        | rdm:Experiment ,rdm:Grant ,rdm:Project ,rdm:Repository ,rdm:Resource ,rdm:Role |
| range         | xsd:string                                                                     |
| definition@en | A description of this Class.                                                   |
| definition@ja | クラスの説明                                                                         |

| Property      | dataAccessRequirements                                                     |
|---------------|----------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/dataAccessRequirements                       |
| subPropertyOf | rdm:description                                                            |
| domain        | rdm:AccessRights                                                           |
| range         | xsd:string                                                                 |
| definition@en | Conditions and method of access to the Resource under access restrictions. |
| definition@ja | アクセス権が限定公開の場合のアクセス条件と方法                                                    |

| Property      | dataDescription                                                              |
|---------------|------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/dataDescription                                |
| subPropertyOf | rdm:description                                                              |
| domain        | rdm:DataManagementPlan                                                       |
| definition@ja | DMPにおけるデータの説明                                                                |
| definition@en | The description of research data to be described in this DataManagementPlan. |

| Property      | measurementTechnique                                            |
|---------------|-----------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/measurementTechnique              |
| subPropertyOf | rdm:description                                                 |
| domain        | rdm:DataManagementPlan                                          |
| range         | xsd:string                                                      |
| definition@en | A technique, method or technology used to create research data. |
| definition@ja | 研究データの収集・取得方法                                                   |

| Property      | operatingSystem                                          |
|---------------|----------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/operatingSystem            |
| subPropertyOf | rdm:description                                          |
| domain        | rdm:SoftwareApplication                                  |
| range         | xsd:string                                               |
| definition@en | Operating systems supported by this SoftwareApplication. |
| definition@ja | アプリケーションがサポートされているOS                                     |

| Property      | processorRequirements                                            |
|---------------|------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/processorRequirements              |
| subPropertyOf | rdm:description                                                  |
| domain        | rdm:SoftwareApplication                                          |
| range         | xsd:string                                                       |
| definition@en | Processor architecture required to run this SoftwareApplication. |
| definition@ja | アプリケーション実行に必要なプロセッサー要件                                           |

| Property      | protocolText                               |
|---------------|--------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/protocolText |
| subPropertyOf | rdm:description                            |
| domain        | rdm:Experiment                             |
| definition@en | A text of protocol of this Experiment.     |
| definition@ja | 実験のプロトコル、手順を示したテキスト                        |

| Property      | purpose                                                                               |
|---------------|---------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/purpose                                                 |
| subPropertyOf | rdm:description                                                                       |
| domain        | rdm:Event                                                                             |
| range         | xsd:string                                                                            |
| definition@en | Context of this Event implementation e.g. reasons and backgrounds for implementation. |
| definition@ja | 実施に至った理由や背景など、イベント実施のコンテクスト                                                           |

| Property      | readme                                                     |
|---------------|------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/readme                       |
| subPropertyOf | rdm:description                                            |
| domain        | rdm:SoftwareApplication                                    |
| definition@en | A text description as Read Me of this SoftwareApplication. |
| definition@ja | README                                                     |

| Property      | softwareRequirements                                            |
|---------------|-----------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/softwareRequirements              |
| subPropertyOf | rdm:description                                                 |
| domain        | rdm:SoftwareApplication                                         |
| range         | xsd:string                                                      |
| definition@en | Component dependency requirements for this SoftwareApplication. |
| definition@ja | アプリケーションコンポーネントの依存要件                                            |

| Property      | specialRequirements                               |
|---------------|---------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/specialRequirements |
| subPropertyOf | rdm:description                                   |
| domain        | rdm:SoftwareApplication                           |
| range         | xsd:string                                        |
| definition@en | Other requirements for this SoftwareApplication.  |
| definition@ja | 他のプロパティに当てはまらないアプリケーションに必要な条件                     |

| Property      | storageRequirements                               |
|---------------|---------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/storageRequirements |
| subPropertyOf | rdm:description                                   |
| domain        | rdm:SoftwareApplication                           |
| range         | xsd:string                                        |
| definition@en | Storage requirements.                             |
| definition@ja | ストレージの要件                                          |

| Property      | detailedRole                               |
|---------------|--------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/detailedRole |
| domain        | rdm:Person                                 |
| range         | xsd:string                                 |
| definition@en | A detailed role of this Person.            |
| definition@ja | 詳細な役割                                      |

| Property      | detailedType                               |
|---------------|--------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/detailedType |
| domain        | rdm:Resource                               |
| range         | xsd:string                                 |
| definition@en | A detailed type of this Resource.          |
| definition@ja | 詳細な資源タイプ                                   |

| Property      | dmpFormat                               |
|---------------|-----------------------------------------|
| IRI           | https://purl.org/rdm/ontology/dmpFormat |
| domain        | rdm:DataManagementPlan                  |
| range         | xsd:string                              |
| definition@en | A name of DataManagementPlan format.    |
| definition@ja | DMP種別名                                  |

| Property      | doi                               |
|---------------|-----------------------------------|
| IRI           | https://purl.org/rdm/ontology/doi |
| domain        | rdm:Project ,rdm:Resource         |
| range         | xsd:anyURI                        |
| definition@ja | DOI                               |
| definition@en | DOI URL.                          |
| seeAlso       | https://www.doi.org/              |

| Property      | email                               |
|---------------|-------------------------------------|
| IRI           | https://purl.org/rdm/ontology/email |
| domain        | rdm:Person                          |
| range         | xsd:string                          |
| definition@en | Email address.                      |
| definition@ja | メールアドレス                             |

| Property      | encodingFormat                               |
|---------------|----------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/encodingFormat |
| domain        | rdm:Resource                                 |
| range         | xsd:string                                   |
| definition@en | A MIME format of this Resource.              |
| definition@ja | リソースのフォーマット                                  |
| seeAlso       | http://www.iana.org/assignments/media-types/ |

| Property      | dataEncodingFormat                                                      |
|---------------|-------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/dataEncodingFormat                        |
| subPropertyOf | rdm:encodingFormat                                                      |
| domain        | rdm:DataManagementPlan                                                  |
| definition@ja | DMPで記述した研究データのフォーマット                                                    |
| definition@en | The format of research data to be described in this DataManagementPlan. |

| Property      | eradResearcherNumber                               |
|---------------|----------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/eradResearcherNumber |
| domain        | rdm:Person                                         |
| range         | xsd:string                                         |
| definition@en | e-rad researcher number.                           |
| definition@ja | e-rad 研究者番号                                        |
| seeAlso       | https://www.e-rad.go.jp/                           |

| Property      | familyName                               |
|---------------|------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/familyName |
| domain        | rdm:Person                               |
| definition@en | Family name.                             |
| definition@ja | 名字                                       |

| Property      | field                                      |
|---------------|--------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/field        |
| domain        | rdm:Project ,rdm:Resource                  |
| range         |                                            |
| definition@en | A research field of this Project/Resource. |
| definition@ja | プロジェクト・リソースの主題                             |

| Property      | funderId                                           |
|---------------|----------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/funderId             |
| domain        | rdm:FundingAgency                                  |
| range         | xsd:string                                         |
| definition@en | Funder ID.                                         |
| definition@ja | 助成機関識別子                                            |
| seeAlso       | https://www.crossref.org/services/funder-registry/ |

| Property      | givenName                               |
|---------------|-----------------------------------------|
| IRI           | https://purl.org/rdm/ontology/givenName |
| domain        | rdm:Person                              |
| definition@en | Given name.                             |
| definition@ja | ファーストネーム                                |

| Property      | hashValue                               |
|---------------|-----------------------------------------|
| IRI           | https://purl.org/rdm/ontology/hashValue |
| domain        | rdm:Resource                            |
| range         | xsd:string                              |
| definition@en | Hash value.                             |
| definition@ja | ハッシュ値                                   |

| Property      | sha256                               |
|---------------|--------------------------------------|
| IRI           | https://purl.org/rdm/ontology/sha256 |
| subPropertyOf | rdm:hashValue                        |
| domain        | rdm:Resource                         |
| range         | xsd:string                           |
| definition@en | sha256 hash value.                   |
| definition@ja | sha256のハッシュ値                         |

| Property      | identifierName                               |
|---------------|----------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/identifierName |
| domain        | rdm:Identifier                               |
| definition@en | A name of identifier scheme e.g. DOI.        |
| definition@ja | 識別子のスキーマ名                                    |

| Property      | identifierValue                               |
|---------------|-----------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/identifierValue |
| domain        | rdm:Identifier                                |
| range         | xsd:anyURI ,xsd:string                        |
| definition@en | Identifier value.                             |
| definition@ja | 識別子の値                                         |

| Property      | doi                               |
|---------------|-----------------------------------|
| IRI           | https://purl.org/rdm/ontology/doi |
| subPropertyOf | rdm:identifierValue               |
| domain        | rdm:Project ,rdm:Resource         |
| range         | xsd:anyURI                        |
| definition@ja | DOI                               |
| definition@en | DOI URL.                          |
| seeAlso       | https://www.doi.org/              |

| Property      | eradResearcherNumber                               |
|---------------|----------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/eradResearcherNumber |
| subPropertyOf | rdm:identifierValue                                |
| domain        | rdm:Person                                         |
| range         | xsd:string                                         |
| definition@en | e-rad researcher number.                           |
| definition@ja | e-rad 研究者番号                                        |
| seeAlso       | https://www.e-rad.go.jp/                           |

| Property      | funderId                                           |
|---------------|----------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/funderId             |
| subPropertyOf | rdm:identifierValue                                |
| domain        | rdm:FundingAgency                                  |
| range         | xsd:string                                         |
| definition@en | Funder ID.                                         |
| definition@ja | 助成機関識別子                                            |
| seeAlso       | https://www.crossref.org/services/funder-registry/ |

| Property      | isbn                               |
|---------------|------------------------------------|
| IRI           | https://purl.org/rdm/ontology/isbn |
| subPropertyOf | rdm:identifierValue                |
| domain        | rdm:Book                           |
| range         | xsd:string                         |
| definition@en | ISBN code.                         |
| definition@ja | ISBNコード                            |

| Property      | japanGrantNumber                               |
|---------------|------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/japanGrantNumber |
| subPropertyOf | rdm:identifierValue                            |
| domain        | rdm:Grant                                      |
| range         | xsd:string                                     |
| definition@en | Japan grant number.                            |
| definition@ja | 体系的課題番号                                        |
| seeAlso       | https://www.nistep.go.jp/archives/53002        |

| Property      | localIdentifier                               |
|---------------|-----------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/localIdentifier |
| subPropertyOf | rdm:identifierValue                           |
| domain        | rdm:Experiment ,rdm:Resource                  |
| definition@en | Local identifier.                             |
| definition@ja | ローカル識別子                                       |

| Property      | orcid                               |
|---------------|-------------------------------------|
| IRI           | https://purl.org/rdm/ontology/orcid |
| subPropertyOf | rdm:identifierValue                 |
| domain        | rdm:Person                          |
| range         | xsd:anyURI                          |
| definition@ja | ORCID iD                            |
| definition@en | ORCID iD.                           |
| seeAlso       | https://orcid.org/                  |

| Property      | raid                               |
|---------------|------------------------------------|
| IRI           | https://purl.org/rdm/ontology/raid |
| subPropertyOf | rdm:identifierValue                |
| domain        | rdm:Project                        |
| range         | xsd:string                         |
| definition@ja | RAiD                               |
| definition@en | RAiD.                              |
| seeAlso       | https://raid.org/                  |

| Property      | ror                               |
|---------------|-----------------------------------|
| IRI           | https://purl.org/rdm/ontology/ror |
| subPropertyOf | rdm:identifierValue               |
| domain        | rdm:Institution                   |
| range         | xsd:anyURI                        |
| definition@ja | ROR ID                            |
| definition@en | ROR ID.                           |
| seeAlso       | https://ror.org/                  |

| Property      | isbn                               |
|---------------|------------------------------------|
| IRI           | https://purl.org/rdm/ontology/isbn |
| domain        | rdm:Book                           |
| range         | xsd:string                         |
| definition@en | ISBN code.                         |
| definition@ja | ISBNコード                            |

| Property      | japanGrantNumber                               |
|---------------|------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/japanGrantNumber |
| domain        | rdm:Grant                                      |
| range         | xsd:string                                     |
| definition@en | Japan grant number.                            |
| definition@ja | 体系的課題番号                                        |
| seeAlso       | https://www.nistep.go.jp/archives/53002        |

| Property      | keywords                                 |
|---------------|------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/keywords   |
| domain        | rdm:Resource                             |
| range         | xsd:string                               |
| definition@en | Keywords used to describe this Resource. |
| definition@ja | キーワード                                    |

| Property      | language                               |
|---------------|----------------------------------------|
| IRI           | https://purl.org/rdm/ontology/language |
| domain        | rdm:Resource                           |
| range         | xsd:language                           |
| definition@en | The language of this Resource.         |
| definition@ja | 言語                                     |

| Property      | localIdentifier                               |
|---------------|-----------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/localIdentifier |
| domain        | rdm:Experiment ,rdm:Resource                  |
| definition@en | Local identifier.                             |
| definition@ja | ローカル識別子                                       |

| Property      | location                                                                  |
|---------------|---------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/location                                    |
| domain        | rdm:Event ,rdm:Resource                                                   |
| range         | xsd:string                                                                |
| definition@en | The place where this Event was/will be held or this Resource was created. |
| definition@ja | 主語クラスの開催場所・取得場所                                                           |

| Property      | measurementTechnique                                            |
|---------------|-----------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/measurementTechnique              |
| domain        | rdm:DataManagementPlan                                          |
| range         | xsd:string                                                      |
| definition@en | A technique, method or technology used to create research data. |
| definition@ja | 研究データの収集・取得方法                                                   |

| Property      | name                                                                                                                             |
|---------------|----------------------------------------------------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/name                                                                                               |
| domain        | rdm:Event ,rdm:Grant ,rdm:Institution ,rdm:License ,rdm:Project ,rdm:Repository ,rdm:Resource ,rdm:Role ,rdm:SoftwareApplication |
| range         | xsd:string                                                                                                                       |
| definition@en | A name of this Class.                                                                                                            |
| definition@ja | 主語クラスの名称                                                                                                                         |

| Property      | additionalName                                       |
|---------------|------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/additionalName         |
| subPropertyOf | rdm:name                                             |
| domain        | rdm:Person                                           |
| definition@en | An additional name for this Person e.g. middle name. |
| definition@ja | ミドルネームなど、その他の名前                                      |

| Property      | familyName                               |
|---------------|------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/familyName |
| subPropertyOf | rdm:name                                 |
| domain        | rdm:Person                               |
| definition@en | Family name.                             |
| definition@ja | 名字                                       |

| Property      | givenName                               |
|---------------|-----------------------------------------|
| IRI           | https://purl.org/rdm/ontology/givenName |
| subPropertyOf | rdm:name                                |
| domain        | rdm:Person                              |
| definition@en | Given name.                             |
| definition@ja | ファーストネーム                                |

| Property      | identifierName                               |
|---------------|----------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/identifierName |
| subPropertyOf | rdm:name                                     |
| domain        | rdm:Identifier                               |
| definition@en | A name of identifier scheme e.g. DOI.        |
| definition@ja | 識別子のスキーマ名                                    |

| Property      | operatingSystem                                          |
|---------------|----------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/operatingSystem            |
| domain        | rdm:SoftwareApplication                                  |
| range         | xsd:string                                               |
| definition@en | Operating systems supported by this SoftwareApplication. |
| definition@ja | アプリケーションがサポートされているOS                                     |

| Property      | orcid                               |
|---------------|-------------------------------------|
| IRI           | https://purl.org/rdm/ontology/orcid |
| domain        | rdm:Person                          |
| range         | xsd:anyURI                          |
| definition@ja | ORCID iD                            |
| definition@en | ORCID iD.                           |
| seeAlso       | https://orcid.org/                  |

| Property      | processorRequirements                                            |
|---------------|------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/processorRequirements              |
| domain        | rdm:SoftwareApplication                                          |
| range         | xsd:string                                                       |
| definition@en | Processor architecture required to run this SoftwareApplication. |
| definition@ja | アプリケーション実行に必要なプロセッサー要件                                           |

| Property      | protocolText                               |
|---------------|--------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/protocolText |
| domain        | rdm:Experiment                             |
| definition@en | A text of protocol of this Experiment.     |
| definition@ja | 実験のプロトコル、手順を示したテキスト                        |

| Property      | purpose                                                                               |
|---------------|---------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/purpose                                                 |
| domain        | rdm:Event                                                                             |
| range         | xsd:string                                                                            |
| definition@en | Context of this Event implementation e.g. reasons and backgrounds for implementation. |
| definition@ja | 実施に至った理由や背景など、イベント実施のコンテクスト                                                           |

| Property      | query                                   |
|---------------|-----------------------------------------|
| IRI           | https://purl.org/rdm/ontology/query     |
| domain        | rdm:Search                              |
| range         | xsd:string                              |
| definition@ja | Search クラスで検索時に使われたクエリ                  |
| definition@en | The query used on this Search activity. |

| Property      | raid                               |
|---------------|------------------------------------|
| IRI           | https://purl.org/rdm/ontology/raid |
| domain        | rdm:Project                        |
| range         | xsd:string                         |
| definition@ja | RAiD                               |
| definition@en | RAiD.                              |
| seeAlso       | https://raid.org/                  |

| Property      | readme                                                     |
|---------------|------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/readme                       |
| domain        | rdm:SoftwareApplication                                    |
| definition@en | A text description as Read Me of this SoftwareApplication. |
| definition@ja | README                                                     |

| Property      | ror                               |
|---------------|-----------------------------------|
| IRI           | https://purl.org/rdm/ontology/ror |
| domain        | rdm:Institution                   |
| range         | xsd:anyURI                        |
| definition@ja | ROR ID                            |
| definition@en | ROR ID.                           |
| seeAlso       | https://ror.org/                  |

| Property      | sdDatePublished                               |
|---------------|-----------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/sdDatePublished |
| domain        | rdm:Resource                                  |
| definition@en | The acquisition date of this Resource.        |
| definition@ja | 外部ファイルの取得日                                    |

| Property      | sha256                               |
|---------------|--------------------------------------|
| IRI           | https://purl.org/rdm/ontology/sha256 |
| domain        | rdm:Resource                         |
| range         | xsd:string                           |
| definition@en | sha256 hash value.                   |
| definition@ja | sha256のハッシュ値                         |

| Property      | size                               |
|---------------|------------------------------------|
| IRI           | https://purl.org/rdm/ontology/size |
| domain        | rdm:Resource                       |
| range         | xsd:nonNegativeInteger ,xsd:string |
| definition@en | This Resource size.                |
| definition@ja | 主語クラスの大きさ、サイズ                      |

| Property      | approximateSize                                                               |
|---------------|-------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/approximateSize                                 |
| subPropertyOf | rdm:size                                                                      |
| domain        | rdm:DataManagementPlan                                                        |
| range         | xsd:string                                                                    |
| definition@en | Approximate size of research data to be described in this DataManagementPlan. |
| definition@ja | DMPにおける概略データ量                                                                 |

| Property      | collectionSize                               |
|---------------|----------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/collectionSize |
| subPropertyOf | rdm:size                                     |
| domain        | rdm:Collection                               |
| range         | xsd:nonNegativeInteger                       |
| definition@en | The number of items in this Collection.      |
| definition@ja | 所定のパッケージに含まれるデータセットの総数                       |

| Property      | softwareRequirements                                            |
|---------------|-----------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/softwareRequirements              |
| domain        | rdm:SoftwareApplication                                         |
| range         | xsd:string                                                      |
| definition@en | Component dependency requirements for this SoftwareApplication. |
| definition@ja | アプリケーションコンポーネントの依存要件                                            |

| Property      | specialRequirements                               |
|---------------|---------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/specialRequirements |
| domain        | rdm:SoftwareApplication                           |
| range         | xsd:string                                        |
| definition@en | Other requirements for this SoftwareApplication.  |
| definition@ja | 他のプロパティに当てはまらないアプリケーションに必要な条件                     |

| Property      | storageRequirements                               |
|---------------|---------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/storageRequirements |
| domain        | rdm:SoftwareApplication                           |
| range         | xsd:string                                        |
| definition@en | Storage requirements.                             |
| definition@ja | ストレージの要件                                          |

| Property      | textContent                               |
|---------------|-------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/textContent |
| domain        | rdm:Resource                              |
| range         | xsd:string                                |
| definition@ja | Resource の内容であるテキスト                       |
| definition@en | The textual content of this Resource.     |

| Property      | url                                                                               |
|---------------|-----------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/url                                                 |
| domain        | rdm:Grant ,rdm:Identifier ,rdm:License ,rdm:Project ,rdm:Repository ,rdm:Resource |
| range         | xsd:anyURI                                                                        |
| definition@en | A URL related to this Class.                                                      |
| definition@ja | 主語クラスに関連するURL                                                                     |

| Property      | value                                                        |
|---------------|--------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/value                          |
| range         | xsd:anyURI ,xsd:double ,xsd:integer ,xsd:string              |
| definition@en | A higer-level property that indicates some value of Classes. |
| definition@ja | クラスにおける何かしらの値を示す上位プロパティ                                      |

| Property      | hashValue                               |
|---------------|-----------------------------------------|
| IRI           | https://purl.org/rdm/ontology/hashValue |
| subPropertyOf | rdm:value                               |
| domain        | rdm:Resource                            |
| range         | xsd:string                              |
| definition@en | Hash value.                             |
| definition@ja | ハッシュ値                                   |

| Property      | sha256                               |
|---------------|--------------------------------------|
| IRI           | https://purl.org/rdm/ontology/sha256 |
| subPropertyOf | rdm:hashValue                        |
| domain        | rdm:Resource                         |
| range         | xsd:string                           |
| definition@en | sha256 hash value.                   |
| definition@ja | sha256のハッシュ値                         |

| Property      | identifierValue                               |
|---------------|-----------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/identifierValue |
| subPropertyOf | rdm:value                                     |
| domain        | rdm:Identifier                                |
| range         | xsd:anyURI ,xsd:string                        |
| definition@en | Identifier value.                             |
| definition@ja | 識別子の値                                         |

| Property      | doi                               |
|---------------|-----------------------------------|
| IRI           | https://purl.org/rdm/ontology/doi |
| subPropertyOf | rdm:identifierValue               |
| domain        | rdm:Project ,rdm:Resource         |
| range         | xsd:anyURI                        |
| definition@ja | DOI                               |
| definition@en | DOI URL.                          |
| seeAlso       | https://www.doi.org/              |

| Property      | eradResearcherNumber                               |
|---------------|----------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/eradResearcherNumber |
| subPropertyOf | rdm:identifierValue                                |
| domain        | rdm:Person                                         |
| range         | xsd:string                                         |
| definition@en | e-rad researcher number.                           |
| definition@ja | e-rad 研究者番号                                        |
| seeAlso       | https://www.e-rad.go.jp/                           |

| Property      | funderId                                           |
|---------------|----------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/funderId             |
| subPropertyOf | rdm:identifierValue                                |
| domain        | rdm:FundingAgency                                  |
| range         | xsd:string                                         |
| definition@en | Funder ID.                                         |
| definition@ja | 助成機関識別子                                            |
| seeAlso       | https://www.crossref.org/services/funder-registry/ |

| Property      | isbn                               |
|---------------|------------------------------------|
| IRI           | https://purl.org/rdm/ontology/isbn |
| subPropertyOf | rdm:identifierValue                |
| domain        | rdm:Book                           |
| range         | xsd:string                         |
| definition@en | ISBN code.                         |
| definition@ja | ISBNコード                            |

| Property      | japanGrantNumber                               |
|---------------|------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/japanGrantNumber |
| subPropertyOf | rdm:identifierValue                            |
| domain        | rdm:Grant                                      |
| range         | xsd:string                                     |
| definition@en | Japan grant number.                            |
| definition@ja | 体系的課題番号                                        |
| seeAlso       | https://www.nistep.go.jp/archives/53002        |

| Property      | localIdentifier                               |
|---------------|-----------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/localIdentifier |
| subPropertyOf | rdm:identifierValue                           |
| domain        | rdm:Experiment ,rdm:Resource                  |
| definition@en | Local identifier.                             |
| definition@ja | ローカル識別子                                       |

| Property      | orcid                               |
|---------------|-------------------------------------|
| IRI           | https://purl.org/rdm/ontology/orcid |
| subPropertyOf | rdm:identifierValue                 |
| domain        | rdm:Person                          |
| range         | xsd:anyURI                          |
| definition@ja | ORCID iD                            |
| definition@en | ORCID iD.                           |
| seeAlso       | https://orcid.org/                  |

| Property      | raid                               |
|---------------|------------------------------------|
| IRI           | https://purl.org/rdm/ontology/raid |
| subPropertyOf | rdm:identifierValue                |
| domain        | rdm:Project                        |
| range         | xsd:string                         |
| definition@ja | RAiD                               |
| definition@en | RAiD.                              |
| seeAlso       | https://raid.org/                  |

| Property      | ror                               |
|---------------|-----------------------------------|
| IRI           | https://purl.org/rdm/ontology/ror |
| subPropertyOf | rdm:identifierValue               |
| domain        | rdm:Institution                   |
| range         | xsd:anyURI                        |
| definition@ja | ROR ID                            |
| definition@en | ROR ID.                           |
| seeAlso       | https://ror.org/                  |

| Property      | version                               |
|---------------|---------------------------------------|
| IRI           | https://purl.org/rdm/ontology/version |
| domain        | rdm:Resource ,rdm:SoftwareApplication |
| range         | xsd:nonNegativeInteger ,xsd:string    |
| definition@en | The version of this Class.            |
| definition@ja | バージョン                                 |

### Object Property

| Property      | accessRightsInformation                               |
|---------------|-------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/accessRightsInformation |
| domain        | rdm:Project ,rdm:Resource                             |
| range         | rdm:AccessRights                                      |
| definition@en | Information on access rights of this Class.           |
| definition@ja | クラスのアクセス権関連情報                                         |

| Property      | dataAccessRightsInformation                                              |
|---------------|--------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/dataAccessRightsInformation                |
| subPropertyOf | rdm:accessRightsInformation                                              |
| domain        | rdm:DataManagementPlan                                                   |
| definition@ja | DMPにおけるデータへのアクセス権                                                        |
| definition@en | Information on access rights to be described in this DataManagementPlan. |

| Property      | activityObject                                                                                                          |
|---------------|-------------------------------------------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/activityObject                                                                            |
| domain        | rdm:Activity                                                                                                            |
| range         | rdm:Collection ,rdm:Event ,rdm:Experiment ,rdm:Project ,rdm:Repository ,rdm:Resource ,rdm:Role ,rdm:SoftwareApplication |
| definition@en | An object of the Activity.                                                                                              |
| definition@ja | 行動の対象物                                                                                                                  |

| Property      | affiliation                                          |
|---------------|------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/affiliation            |
| domain        | rdm:Person                                           |
| range         | rdm:Institution                                      |
| definition@en | An organization that this Person is affiliated with. |
| definition@ja | 人物の所属先機関                                             |

| Property      | agent                                            |
|---------------|--------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/agent              |
| domain        | rdm:Activity                                     |
| range         | rdm:Institution ,rdm:Person                      |
| definition@en | The direct performer or driver of this Activity. |
| definition@ja | 行動・行為の直接的な実施者                                    |

| Property      | cites                                                                                            |
|---------------|--------------------------------------------------------------------------------------------------|
| inverseOf     | rdm:isCitedBy                                                                                    |
| domain        | rdm:Resource                                                                                     |
| range         | rdm:Resource                                                                                     |
| definition@en | A Resource that this Class cites.                                                                |
| definition@ja | 主語クラスが引用しているリソース                                                                                 |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#cites |

| Property      | collectedIn                                                          |
|---------------|----------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/collectedIn                            |
| inverseOf     | rdm:collectionItem                                                   |
| domain        | rdm:Resource                                                         |
| range         | rdm:Collection                                                       |
| definition@en | A Collection which includes this Resource as a member of Collection. |
| definition@ja | リソースをメンバーとして含むCollection                                             |

| Property      | collectionItem                          |
|---------------|-----------------------------------------|
| domain        | rdm:Collection                          |
| range         | rdm:Resource                            |
| definition@en | A Resource included in this Collection. |
| definition@ja | コレクションに含まれるリソース                         |

| Property      | collects                                                                                            |
|---------------|-----------------------------------------------------------------------------------------------------|
| inverseOf     | rdm:isCollectedBy                                                                                   |
| domain        | rdm:Collection ,rdm:Resource ,rdm:SoftwareApplication                                               |
| range         | rdm:Collection ,rdm:Resource ,rdm:SoftwareApplication                                               |
| definition@en | A Class which collected/created by using this Class.                                                |
| definition@ja | 主語クラスを使用して収集・作成されたクラス                                                                               |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#collects |

| Property      | compiles                                                                                            |
|---------------|-----------------------------------------------------------------------------------------------------|
| inverseOf     | rdm:isCompiledBy                                                                                    |
| domain        | rdm:Resource ,rdm:SoftwareApplication                                                               |
| range         | rdm:Resource ,rdm:SoftwareApplication                                                               |
| definition@en | The result of a compile or creation event using this Class.                                         |
| definition@ja | 主語クラスを使用したコンパイルまたは作成イベントの結果                                                                         |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#compiles |

| Property      | conditionOfAccess                               |
|---------------|-------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/conditionOfAccess |
| domain        | rdm:AccessRights                                |
| range         | rdm:RightsStatement                             |
| definition@en | Access rights type.                             |
| definition@ja | アクセス権の種別                                        |

| Property      | continues                                                                                            |
|---------------|------------------------------------------------------------------------------------------------------|
| inverseOf     | rdm:isContinuedBy                                                                                    |
| domain        | rdm:Event ,rdm:Institution ,rdm:Project ,rdm:Repository ,rdm:Resource ,rdm:SoftwareApplication       |
| range         | rdm:Event ,rdm:Institution ,rdm:Project ,rdm:Repository ,rdm:Resource ,rdm:SoftwareApplication       |
| definition@en | A Class of which this Class is a continuation.                                                       |
| definition@ja | 主語クラスが継続しているクラス                                                                                      |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#continues |

| Property      | contributor                                                                                   |
|---------------|-----------------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/contributor                                                     |
| domain        | rdm:Collection ,rdm:Event ,rdm:Experiment ,rdm:Project ,rdm:Resource ,rdm:SoftwareApplication |
| range         | rdm:Institution ,rdm:Person                                                                   |
| definition@en | A contributor to this Class.                                                                  |
| definition@ja | クラスへの寄与者                                                                                      |

| Property      | creator                               |
|---------------|---------------------------------------|
| IRI           | https://purl.org/rdm/ontology/creator |
| subPropertyOf | rdm:contributor                       |
| domain        | rdm:Resource ,rdm:SoftwareApplication |
| range         | rdm:Person                            |
| definition@en | The creator/author of this Resource.  |
| definition@ja | リソースの作成者                              |

| Property      | dataCreator                                                              |
|---------------|--------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/dataCreator                                |
| subPropertyOf | rdm:creator                                                              |
| domain        | rdm:DataManagementPlan                                                   |
| range         | rdm:Person                                                               |
| definition@ja | DMPにおける研究データの作成者                                                         |
| definition@en | The creator of research data to be described in this DataManagementPlan. |

| Property      | dataManager                                                                   |
|---------------|-------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/dataManager                                     |
| subPropertyOf | rdm:contributor                                                               |
| domain        | rdm:DataManagementPlan                                                        |
| range         | rdm:Person                                                                    |
| definition@ja | DMPにおける研究データ管理者                                                               |
| definition@en | The data manager of research data to be described in this DataManagementPlan. |

| Property      | experimenter                                                 |
|---------------|--------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/experimenter                   |
| subPropertyOf | rdm:contributor                                              |
| domain        | rdm:Experiment                                               |
| range         | rdm:Person                                                   |
| definition@en | The practitioner, performer and executor of this Experiment. |
| definition@ja | 実験の実施者、実行者                                                   |

| Property      | hostingInstitution                                                                                             |
|---------------|----------------------------------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/hostingInstitution                                                               |
| subPropertyOf | rdm:contributor                                                                                                |
| domain        | rdm:DataManagementPlan ,rdm:Project ,rdm:Resource                                                              |
| range         | rdm:Institution                                                                                                |
| definition@ja | (Project に属する)Resource の管理機関、もしくはDMPにおける研究データ管理機関                                                              |
| definition@en | The hosting institution of Resource (in Project) and research data to be described in this DataManagementPlan. |

| Property      | identifierManager                                                          |
|---------------|----------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/identifierManager                            |
| subPropertyOf | rdm:contributor                                                            |
| domain        | rdm:Identifier                                                             |
| range         | rdm:Institution                                                            |
| definition@en | A manager of identifier scheme/service, e.g. International DOI Foundation. |
| definition@ja | 国際DOI財団など、識別子の管理者                                                          |

| Property      | organizer                               |
|---------------|-----------------------------------------|
| IRI           | https://purl.org/rdm/ontology/organizer |
| subPropertyOf | rdm:contributor                         |
| domain        | rdm:Event                               |
| definition@en | An Event organizer or host.             |
| definition@ja | イベントの開催者、主催者                            |

| Property      | researcher                               |
|---------------|------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/researcher |
| subPropertyOf | rdm:contributor                          |
| domain        | rdm:Project                              |
| range         | rdm:Person                               |
| definition@en | A researcher involved in this Project.   |
| definition@ja | プロジェクトに参加した研究者                           |

| Property      | creator                               |
|---------------|---------------------------------------|
| domain        | rdm:Resource ,rdm:SoftwareApplication |
| range         | rdm:Person                            |
| definition@en | The creator/author of this Resource.  |
| definition@ja | リソースの作成者                              |

| Property      | dataCreator                                                              |
|---------------|--------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/dataCreator                                |
| subPropertyOf | rdm:creator                                                              |
| domain        | rdm:DataManagementPlan                                                   |
| range         | rdm:Person                                                               |
| definition@ja | DMPにおける研究データの作成者                                                         |
| definition@en | The creator of research data to be described in this DataManagementPlan. |

| Property      | dataAccessRightsInformation                                              |
|---------------|--------------------------------------------------------------------------|
| domain        | rdm:DataManagementPlan                                                   |
| definition@ja | DMPにおけるデータへのアクセス権                                                        |
| definition@en | Information on access rights to be described in this DataManagementPlan. |

| Property      | dataCreator                                                              |
|---------------|--------------------------------------------------------------------------|
| domain        | rdm:DataManagementPlan                                                   |
| range         | rdm:Person                                                               |
| definition@ja | DMPにおける研究データの作成者                                                         |
| definition@en | The creator of research data to be described in this DataManagementPlan. |

| Property      | dataIdentifier                                                              |
|---------------|-----------------------------------------------------------------------------|
| domain        | rdm:DataManagementPlan                                                      |
| range         | rdm:Identifier                                                              |
| definition@ja | DMPにおけるデータ識別子                                                               |
| definition@en | The identifier of research data to be described in this DataManagementPlan. |

| Property      | dataLicenseInformation                                                   |
|---------------|--------------------------------------------------------------------------|
| domain        | rdm:DataManagementPlan                                                   |
| definition@ja | DMPにおけるデータのライセンス                                                         |
| definition@en | The license of research data to be described in this DataManagementPlan. |

| Property      | dataManager                                                                   |
|---------------|-------------------------------------------------------------------------------|
| domain        | rdm:DataManagementPlan                                                        |
| range         | rdm:Person                                                                    |
| definition@ja | DMPにおける研究データ管理者                                                               |
| definition@en | The data manager of research data to be described in this DataManagementPlan. |

| Property      | describes                                                                                            |
|---------------|------------------------------------------------------------------------------------------------------|
| inverseOf     | rdm:isDescribedBy                                                                                    |
| domain        | rdm:Resource                                                                                         |
| definition@en | A Class that this Resource describes.                                                                |
| definition@ja | Resource が説明しているクラス                                                                                  |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#continues |

| Property      | dmp                                                        |
|---------------|------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/dmp                          |
| domain        | rdm:Project ,rdm:Resource                                  |
| range         | rdm:DataManagementPlan                                     |
| definition@en | Contents of data management plan of this Project/Resource. |
| definition@ja | 資源やプロジェクトに紐づくデータ管理計画                                       |

| Property      | dmpFormatProvider                                            |
|---------------|--------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/dmpFormatProvider              |
| domain        | rdm:DataManagementPlan                                       |
| range         | rdm:Institution                                              |
| definition@en | A institution which provides this DataManagementPlan format. |
| definition@ja | DMP種別の提供者                                                    |

| Property      | dmpTargetItem                               |
|---------------|---------------------------------------------|
| domain        | rdm:DataManagementPlan                      |
| range         | rdm:Resource                                |
| definition@en | A Resource described in DataManagementPlan. |
| definition@ja | DMPで対象になっているリソース                            |

| Property      | documents                                                                                            |
|---------------|------------------------------------------------------------------------------------------------------|
| inverseOf     | rdm:isDocumentedBy                                                                                   |
| domain        | rdm:Resource                                                                                         |
| range         | rdm:SoftwareApplication                                                                              |
| definition@en | A  SoftwareApplication which is documented by this Resource.                                         |
| definition@ja | Resource がその説明文書・ドキュメントに相当する SoftwareApplication                                                     |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#documents |

| Property      | experimenter                                                 |
|---------------|--------------------------------------------------------------|
| domain        | rdm:Experiment                                               |
| range         | rdm:Person                                                   |
| definition@en | The practitioner, performer and executor of this Experiment. |
| definition@ja | 実験の実施者、実行者                                                   |

| Property      | fromLocation                            |
|---------------|-----------------------------------------|
| domain        | rdm:Download ,rdm:Upload                |
| range         | rdm:Repository ,rdm:SoftwareApplication |
| definition@en | Uploaded or downloaded from             |
| definition@ja | アップロードもしくはダウンロード元                       |

| Property      | funder                                                                                  |
|---------------|-----------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/funder                                                    |
| domain        | rdm:Grant ,rdm:Project ,rdm:Resource                                                    |
| range         | rdm:FundingAgency                                                                       |
| definition@en | An organization that funds this Project or research activities to create this Resource. |
| definition@ja | 研究資金プログラム提供者                                                                            |

| Property      | funding                                                                          |
|---------------|----------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/funding                                            |
| domain        | rdm:Project ,rdm:Resource                                                        |
| range         | rdm:Grant                                                                        |
| definition@en | A grant program for this Project or research activities to create this Resource. |
| definition@ja | 研究資金プログラム                                                                        |

| Property      | hasMetadata                                                                                          |
|---------------|------------------------------------------------------------------------------------------------------|
| inverseOf     | rdm:isMetadataFor                                                                                    |
| domain        | rdm:Collection ,rdm:Project ,rdm:Resource                                                            |
| range         | rdm:MetadataDocument                                                                                 |
| definition@en | A Resource which has additional metadata of this Class.                                              |
| definition@ja | 主語クラスの追加メタデータを持つ Resource                                                                            |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#continues |

| Property      | hasPart                                                                                                        |
|---------------|----------------------------------------------------------------------------------------------------------------|
| inverseOf     | rdm:isPartOf                                                                                                   |
| domain        | rdm:Collection ,rdm:Experiment ,rdm:Grant ,rdm:Institution ,rdm:Project ,rdm:Resource ,rdm:SoftwareApplication |
| definition@en | A class consisting of multiple parts of which this class is a part.                                            |
| definition@ja | 主語クラスが一部分となっている、複数の部分から成るクラス                                                                                   |

| Property      | hasVersion                                                                                               |
|---------------|----------------------------------------------------------------------------------------------------------|
| inverseOf     | rdm:isVersionOf                                                                                          |
| domain        | rdm:Collection ,rdm:Resource ,rdm:SoftwareApplication                                                    |
| range         | rdm:Collection ,rdm:Resource ,rdm:SoftwareApplication                                                    |
| definition@en | A Class  which is another version of this Class.                                                         |
| definition@ja | 主語クラスの異なるバージョンとして存在するクラス                                                                                 |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#ismetadatafor |

| Property      | hostingInstitution                                                                                             |
|---------------|----------------------------------------------------------------------------------------------------------------|
| domain        | rdm:DataManagementPlan ,rdm:Project ,rdm:Resource                                                              |
| range         | rdm:Institution                                                                                                |
| definition@ja | (Project に属する)Resource の管理機関、もしくはDMPにおける研究データ管理機関                                                              |
| definition@en | The hosting institution of Resource (in Project) and research data to be described in this DataManagementPlan. |

| Property      | identifierInformation                                                                             |
|---------------|---------------------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/identifierInformation                                               |
| domain        | rdm:Collection ,rdm:Grant ,rdm:Institution ,rdm:Person ,rdm:Project ,rdm:Repository ,rdm:Resource |
| range         | rdm:Identifier                                                                                    |
| definition@en | An identifier information of this Class.                                                          |
| definition@ja | 識別子                                                                                               |

| Property      | dataIdentifier                                                              |
|---------------|-----------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/dataIdentifier                                |
| subPropertyOf | rdm:identifierInformation                                                   |
| domain        | rdm:DataManagementPlan                                                      |
| range         | rdm:Identifier                                                              |
| definition@ja | DMPにおけるデータ識別子                                                               |
| definition@en | The identifier of research data to be described in this DataManagementPlan. |

| Property      | identifierManager                                                          |
|---------------|----------------------------------------------------------------------------|
| domain        | rdm:Identifier                                                             |
| range         | rdm:Institution                                                            |
| definition@en | A manager of identifier scheme/service, e.g. International DOI Foundation. |
| definition@ja | 国際DOI財団など、識別子の管理者                                                          |

| Property      | inProject                                      |
|---------------|------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/inProject        |
| inverseOf     | rdm:projectItem                                |
| domain        | rdm:Resource                                   |
| range         | rdm:Project                                    |
| definition@en | A Project this Resource is within/included in. |
| definition@ja | リソースが属するプロジェクト                                 |

| Property      | inclusionRelation                                                              |
|---------------|--------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/inclusionRelation                                |
| definition@en | A higher-level property that indicates inclusion relationship between Classes. |
| definition@ja | 主語クラスと包含関係のあるクラスを指す上位プロパティ                                                     |

| Property      | hasPart                                                                                                        |
|---------------|----------------------------------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/hasPart                                                                          |
| subPropertyOf | rdm:inclusionRelation                                                                                          |
| inverseOf     | rdm:isPartOf                                                                                                   |
| domain        | rdm:Collection ,rdm:Experiment ,rdm:Grant ,rdm:Institution ,rdm:Project ,rdm:Resource ,rdm:SoftwareApplication |
| definition@en | A class consisting of multiple parts of which this class is a part.                                            |
| definition@ja | 主語クラスが一部分となっている、複数の部分から成るクラス                                                                                   |

| Property      | isPartOf                                                                                                       |
|---------------|----------------------------------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/isPartOf                                                                         |
| subPropertyOf | rdm:inclusionRelation                                                                                          |
| domain        | rdm:Collection ,rdm:Experiment ,rdm:Grant ,rdm:Institution ,rdm:Project ,rdm:Resource ,rdm:SoftwareApplication |
| definition@en | A Class of the parts that make up this class                                                                   |
| definition@ja | 主語クラスを構成する部分のクラス                                                                                               |

| Property      | instrument                                                                        |
|---------------|-----------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/instrument                                          |
| domain        | rdm:Activity ,rdm:Experiment                                                      |
| definition@en | The object that helped the agent perform the Activity and used in the Experiment. |
| definition@ja | 行動や実験で使われた道具、ツール                                                                  |

| Property      | isCitedBy                                                                                            |
|---------------|------------------------------------------------------------------------------------------------------|
| domain        | rdm:Resource                                                                                         |
| range         | rdm:Resource                                                                                         |
| definition@en | A Resource that this Class is cited.                                                                 |
| definition@ja | 主語クラスが引用されているリソース                                                                                    |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#iscitedby |

| Property      | isCollectedBy                                                                                            |
|---------------|----------------------------------------------------------------------------------------------------------|
| domain        | rdm:Collection ,rdm:Resource ,rdm:SoftwareApplication                                                    |
| range         | rdm:Collection ,rdm:Resource ,rdm:SoftwareApplication                                                    |
| definition@en | A Class that is used to collect/create this Class.                                                       |
| definition@ja | 主語クラスの収集・生成に利用されたクラス                                                                                     |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#iscollectedby |

| Property      | isCompiledBy                                                                                            |
|---------------|---------------------------------------------------------------------------------------------------------|
| domain        | rdm:Resource ,rdm:SoftwareApplication                                                                   |
| range         | rdm:Resource ,rdm:SoftwareApplication                                                                   |
| definition@en | A Class used to compile or create this Class.                                                           |
| definition@ja | 主語クラスをコンパイルまたは作成するために使用するクラス                                                                            |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#iscompiledby |

| Property      | isContinuedBy                                                                                            |
|---------------|----------------------------------------------------------------------------------------------------------|
| domain        | rdm:Event ,rdm:Institution ,rdm:Project ,rdm:Repository ,rdm:Resource ,rdm:SoftwareApplication           |
| range         | rdm:Event ,rdm:Institution ,rdm:Project ,rdm:Repository ,rdm:Resource ,rdm:SoftwareApplication           |
| definition@en | A Class continued by this Class                                                                          |
| definition@ja | 主語クラスが継続されているクラス                                                                                         |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#iscontinuedby |

| Property      | isDerivedFrom                                                                                            |
|---------------|----------------------------------------------------------------------------------------------------------|
| inverseOf     | rdm:isSourceOf                                                                                           |
| domain        | rdm:Collection ,rdm:Project ,rdm:Resource                                                                |
| range         | rdm:Collection ,rdm:Project ,rdm:Resource                                                                |
| definition@en | A Class on which this Class is based.                                                                    |
| definition@ja | 主語クラスが基づいているクラス                                                                                          |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#isderivedfrom |

| Property      | isDescribedBy                                                                                        |
|---------------|------------------------------------------------------------------------------------------------------|
| range         | rdm:Resource                                                                                         |
| definition@en | A Resource that describes this Class.                                                                |
| definition@ja | 主語クラスを説明している Resource                                                                                |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#continues |

| Property      | isDocumentedBy                                                                                            |
|---------------|-----------------------------------------------------------------------------------------------------------|
| domain        | rdm:SoftwareApplication                                                                                   |
| range         | rdm:Resource                                                                                              |
| definition@en | A Resource which is documentation about/explaining this SoftwareApplication.                              |
| definition@ja | SoftwareApplication の説明文書・ドキュメントである Resource                                                              |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#isdocumentedby |

| Property      | isIdenticalTo                                                                                            |
|---------------|----------------------------------------------------------------------------------------------------------|
| domain        | rdm:Resource                                                                                             |
| definition@en | A Resource which is identical to this Resource.                                                          |
| definition@ja | 主語クラスと同一である Resource                                                                                     |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#isidenticalto |

| Property      | isMetadataFor                                                                                            |
|---------------|----------------------------------------------------------------------------------------------------------|
| domain        | rdm:MetadataDocument                                                                                     |
| range         | rdm:Collection ,rdm:Project ,rdm:Resource                                                                |
| definition@en | A Class for which this Resource has additional metadata.                                                 |
| definition@ja | Resource が追加メタデータになっているクラス                                                                               |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#ismetadatafor |

| Property      | isNewVersionOf                                                                                            |
|---------------|-----------------------------------------------------------------------------------------------------------|
| inverseOf     | rdm:isPreviousVersionOf                                                                                   |
| domain        | rdm:Collection ,rdm:Resource ,rdm:SoftwareApplication                                                     |
| range         | rdm:Collection ,rdm:Resource ,rdm:SoftwareApplication                                                     |
| definition@en | A Class which is a new edition of this Class.                                                             |
| definition@ja | 主語クラスが新版に当たる、旧版のクラス                                                                                       |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#isnewversionof |

| Property      | isObsoletedBy                                                                                            |
|---------------|----------------------------------------------------------------------------------------------------------|
| inverseOf     | rdm:obsoletes                                                                                            |
| definition@en | A Class which replaces this Class.                                                                       |
| definition@ja | 主語クラスを廃止させたクラス                                                                                           |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#isobsoletedby |

| Property      | isOriginalFormOf                                                                                            |
|---------------|-------------------------------------------------------------------------------------------------------------|
| inverseOf     | rdm:isVariantFormOf                                                                                         |
| domain        | rdm:Resource ,rdm:SoftwareApplication                                                                       |
| range         | rdm:Resource ,rdm:SoftwareApplication                                                                       |
| definition@en | A Class of which this Class is the original form.                                                           |
| definition@ja | 主語クラスをオリジナルとするクラス                                                                                           |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#isoriginalformof |

| Property      | isPartOf                                                                                                       |
|---------------|----------------------------------------------------------------------------------------------------------------|
| domain        | rdm:Collection ,rdm:Experiment ,rdm:Grant ,rdm:Institution ,rdm:Project ,rdm:Resource ,rdm:SoftwareApplication |
| definition@en | A Class of the parts that make up this class                                                                   |
| definition@ja | 主語クラスを構成する部分のクラス                                                                                               |

| Property      | isPreviousVersionOf                                                                                            |
|---------------|----------------------------------------------------------------------------------------------------------------|
| domain        | rdm:Collection ,rdm:Resource ,rdm:SoftwareApplication                                                          |
| range         | rdm:Collection ,rdm:Resource ,rdm:SoftwareApplication                                                          |
| definition@en | A Class which is a previous edition of this Class.                                                             |
| definition@ja | 主語クラスが旧版に当たる、新版のクラス                                                                                            |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#ispreviousversionof |

| Property      | isPublishedIn                                                                                                  |
|---------------|----------------------------------------------------------------------------------------------------------------|
| domain        | rdm:Collection ,rdm:Project ,rdm:Resource ,rdm:SoftwareApplication                                             |
| range         | rdm:Collection ,rdm:Project ,rdm:Resource ,rdm:SoftwareApplication                                             |
| definition@en | A Class which is published in this Class.                                                                      |
| definition@ja | 主語クラスをその一部として公開するクラス                                                                                           |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#ispreviousversionof |

| Property      | isReferencedBy                                                                                            |
|---------------|-----------------------------------------------------------------------------------------------------------|
| inverseOf     | rdm:references                                                                                            |
| domain        | rdm:Collection ,rdm:Project ,rdm:Resource ,rdm:SoftwareApplication                                        |
| range         | rdm:Collection ,rdm:Project ,rdm:Resource ,rdm:SoftwareApplication                                        |
| definition@en | A Class which uses this Class as a source of information.                                                 |
| definition@ja | 主語クラスを情報源として参照しているクラス                                                                                     |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#isreferencedby |

| Property      | isRelatedTo                                                      |
|---------------|------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/isRelatedTo                        |
| definition@en | A Class independent of this Class that is related to this Class. |
| definition@ja | 主語クラスと何らかの関連がある、独立したクラス                                          |

| Property      | cites                                                                                            |
|---------------|--------------------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/cites                                                              |
| subPropertyOf | rdm:isRelatedTo                                                                                  |
| inverseOf     | rdm:isCitedBy                                                                                    |
| domain        | rdm:Resource                                                                                     |
| range         | rdm:Resource                                                                                     |
| definition@en | A Resource that this Class cites.                                                                |
| definition@ja | 主語クラスが引用しているリソース                                                                                 |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#cites |

| Property      | collects                                                                                            |
|---------------|-----------------------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/collects                                                              |
| subPropertyOf | rdm:isRelatedTo                                                                                     |
| inverseOf     | rdm:isCollectedBy                                                                                   |
| domain        | rdm:Collection ,rdm:Resource ,rdm:SoftwareApplication                                               |
| range         | rdm:Collection ,rdm:Resource ,rdm:SoftwareApplication                                               |
| definition@en | A Class which collected/created by using this Class.                                                |
| definition@ja | 主語クラスを使用して収集・作成されたクラス                                                                               |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#collects |

| Property      | compiles                                                                                            |
|---------------|-----------------------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/compiles                                                              |
| subPropertyOf | rdm:isRelatedTo                                                                                     |
| inverseOf     | rdm:isCompiledBy                                                                                    |
| domain        | rdm:Resource ,rdm:SoftwareApplication                                                               |
| range         | rdm:Resource ,rdm:SoftwareApplication                                                               |
| definition@en | The result of a compile or creation event using this Class.                                         |
| definition@ja | 主語クラスを使用したコンパイルまたは作成イベントの結果                                                                         |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#compiles |

| Property      | continues                                                                                            |
|---------------|------------------------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/continues                                                              |
| subPropertyOf | rdm:isRelatedTo                                                                                      |
| inverseOf     | rdm:isContinuedBy                                                                                    |
| domain        | rdm:Event ,rdm:Institution ,rdm:Project ,rdm:Repository ,rdm:Resource ,rdm:SoftwareApplication       |
| range         | rdm:Event ,rdm:Institution ,rdm:Project ,rdm:Repository ,rdm:Resource ,rdm:SoftwareApplication       |
| definition@en | A Class of which this Class is a continuation.                                                       |
| definition@ja | 主語クラスが継続しているクラス                                                                                      |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#continues |

| Property      | describes                                                                                            |
|---------------|------------------------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/describes                                                              |
| subPropertyOf | rdm:isRelatedTo                                                                                      |
| inverseOf     | rdm:isDescribedBy                                                                                    |
| domain        | rdm:Resource                                                                                         |
| definition@en | A Class that this Resource describes.                                                                |
| definition@ja | Resource が説明しているクラス                                                                                  |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#continues |

| Property      | documents                                                                                            |
|---------------|------------------------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/documents                                                              |
| subPropertyOf | rdm:isRelatedTo                                                                                      |
| inverseOf     | rdm:isDocumentedBy                                                                                   |
| domain        | rdm:Resource                                                                                         |
| range         | rdm:SoftwareApplication                                                                              |
| definition@en | A  SoftwareApplication which is documented by this Resource.                                         |
| definition@ja | Resource がその説明文書・ドキュメントに相当する SoftwareApplication                                                     |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#documents |

| Property      | hasMetadata                                                                                          |
|---------------|------------------------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/hasMetadata                                                            |
| subPropertyOf | rdm:isRelatedTo                                                                                      |
| inverseOf     | rdm:isMetadataFor                                                                                    |
| domain        | rdm:Collection ,rdm:Project ,rdm:Resource                                                            |
| range         | rdm:MetadataDocument                                                                                 |
| definition@en | A Resource which has additional metadata of this Class.                                              |
| definition@ja | 主語クラスの追加メタデータを持つ Resource                                                                            |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#continues |

| Property      | hasVersion                                                                                               |
|---------------|----------------------------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/hasVersion                                                                 |
| subPropertyOf | rdm:isRelatedTo                                                                                          |
| inverseOf     | rdm:isVersionOf                                                                                          |
| domain        | rdm:Collection ,rdm:Resource ,rdm:SoftwareApplication                                                    |
| range         | rdm:Collection ,rdm:Resource ,rdm:SoftwareApplication                                                    |
| definition@en | A Class  which is another version of this Class.                                                         |
| definition@ja | 主語クラスの異なるバージョンとして存在するクラス                                                                                 |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#ismetadatafor |

| Property      | isCitedBy                                                                                            |
|---------------|------------------------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/isCitedBy                                                              |
| subPropertyOf | rdm:isRelatedTo                                                                                      |
| domain        | rdm:Resource                                                                                         |
| range         | rdm:Resource                                                                                         |
| definition@en | A Resource that this Class is cited.                                                                 |
| definition@ja | 主語クラスが引用されているリソース                                                                                    |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#iscitedby |

| Property      | isCollectedBy                                                                                            |
|---------------|----------------------------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/isCollectedBy                                                              |
| subPropertyOf | rdm:isRelatedTo                                                                                          |
| domain        | rdm:Collection ,rdm:Resource ,rdm:SoftwareApplication                                                    |
| range         | rdm:Collection ,rdm:Resource ,rdm:SoftwareApplication                                                    |
| definition@en | A Class that is used to collect/create this Class.                                                       |
| definition@ja | 主語クラスの収集・生成に利用されたクラス                                                                                     |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#iscollectedby |

| Property      | isCompiledBy                                                                                            |
|---------------|---------------------------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/isCompiledBy                                                              |
| subPropertyOf | rdm:isRelatedTo                                                                                         |
| domain        | rdm:Resource ,rdm:SoftwareApplication                                                                   |
| range         | rdm:Resource ,rdm:SoftwareApplication                                                                   |
| definition@en | A Class used to compile or create this Class.                                                           |
| definition@ja | 主語クラスをコンパイルまたは作成するために使用するクラス                                                                            |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#iscompiledby |

| Property      | isContinuedBy                                                                                            |
|---------------|----------------------------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/isContinuedBy                                                              |
| subPropertyOf | rdm:isRelatedTo                                                                                          |
| domain        | rdm:Event ,rdm:Institution ,rdm:Project ,rdm:Repository ,rdm:Resource ,rdm:SoftwareApplication           |
| range         | rdm:Event ,rdm:Institution ,rdm:Project ,rdm:Repository ,rdm:Resource ,rdm:SoftwareApplication           |
| definition@en | A Class continued by this Class                                                                          |
| definition@ja | 主語クラスが継続されているクラス                                                                                         |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#iscontinuedby |

| Property      | isDerivedFrom                                                                                            |
|---------------|----------------------------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/isDerivedFrom                                                              |
| subPropertyOf | rdm:isRelatedTo                                                                                          |
| inverseOf     | rdm:isSourceOf                                                                                           |
| domain        | rdm:Collection ,rdm:Project ,rdm:Resource                                                                |
| range         | rdm:Collection ,rdm:Project ,rdm:Resource                                                                |
| definition@en | A Class on which this Class is based.                                                                    |
| definition@ja | 主語クラスが基づいているクラス                                                                                          |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#isderivedfrom |

| Property      | isDescribedBy                                                                                        |
|---------------|------------------------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/isDescribedBy                                                          |
| subPropertyOf | rdm:isRelatedTo                                                                                      |
| range         | rdm:Resource                                                                                         |
| definition@en | A Resource that describes this Class.                                                                |
| definition@ja | 主語クラスを説明している Resource                                                                                |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#continues |

| Property      | isDocumentedBy                                                                                            |
|---------------|-----------------------------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/isDocumentedBy                                                              |
| subPropertyOf | rdm:isRelatedTo                                                                                           |
| domain        | rdm:SoftwareApplication                                                                                   |
| range         | rdm:Resource                                                                                              |
| definition@en | A Resource which is documentation about/explaining this SoftwareApplication.                              |
| definition@ja | SoftwareApplication の説明文書・ドキュメントである Resource                                                              |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#isdocumentedby |

| Property      | isIdenticalTo                                                                                            |
|---------------|----------------------------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/isIdenticalTo                                                              |
| subPropertyOf | rdm:isRelatedTo                                                                                          |
| domain        | rdm:Resource                                                                                             |
| definition@en | A Resource which is identical to this Resource.                                                          |
| definition@ja | 主語クラスと同一である Resource                                                                                     |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#isidenticalto |

| Property      | isMetadataFor                                                                                            |
|---------------|----------------------------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/isMetadataFor                                                              |
| subPropertyOf | rdm:isRelatedTo                                                                                          |
| domain        | rdm:MetadataDocument                                                                                     |
| range         | rdm:Collection ,rdm:Project ,rdm:Resource                                                                |
| definition@en | A Class for which this Resource has additional metadata.                                                 |
| definition@ja | Resource が追加メタデータになっているクラス                                                                               |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#ismetadatafor |

| Property      | isNewVersionOf                                                                                            |
|---------------|-----------------------------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/isNewVersionOf                                                              |
| subPropertyOf | rdm:isRelatedTo                                                                                           |
| inverseOf     | rdm:isPreviousVersionOf                                                                                   |
| domain        | rdm:Collection ,rdm:Resource ,rdm:SoftwareApplication                                                     |
| range         | rdm:Collection ,rdm:Resource ,rdm:SoftwareApplication                                                     |
| definition@en | A Class which is a new edition of this Class.                                                             |
| definition@ja | 主語クラスが新版に当たる、旧版のクラス                                                                                       |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#isnewversionof |

| Property      | isObsoletedBy                                                                                            |
|---------------|----------------------------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/isObsoletedBy                                                              |
| subPropertyOf | rdm:isRelatedTo                                                                                          |
| inverseOf     | rdm:obsoletes                                                                                            |
| definition@en | A Class which replaces this Class.                                                                       |
| definition@ja | 主語クラスを廃止させたクラス                                                                                           |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#isobsoletedby |

| Property      | isOriginalFormOf                                                                                            |
|---------------|-------------------------------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/isOriginalFormOf                                                              |
| subPropertyOf | rdm:isRelatedTo                                                                                             |
| inverseOf     | rdm:isVariantFormOf                                                                                         |
| domain        | rdm:Resource ,rdm:SoftwareApplication                                                                       |
| range         | rdm:Resource ,rdm:SoftwareApplication                                                                       |
| definition@en | A Class of which this Class is the original form.                                                           |
| definition@ja | 主語クラスをオリジナルとするクラス                                                                                           |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#isoriginalformof |

| Property      | isPreviousVersionOf                                                                                            |
|---------------|----------------------------------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/isPreviousVersionOf                                                              |
| subPropertyOf | rdm:isRelatedTo                                                                                                |
| domain        | rdm:Collection ,rdm:Resource ,rdm:SoftwareApplication                                                          |
| range         | rdm:Collection ,rdm:Resource ,rdm:SoftwareApplication                                                          |
| definition@en | A Class which is a previous edition of this Class.                                                             |
| definition@ja | 主語クラスが旧版に当たる、新版のクラス                                                                                            |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#ispreviousversionof |

| Property      | isPublishedIn                                                                                                  |
|---------------|----------------------------------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/isPublishedIn                                                                    |
| subPropertyOf | rdm:isRelatedTo                                                                                                |
| domain        | rdm:Collection ,rdm:Project ,rdm:Resource ,rdm:SoftwareApplication                                             |
| range         | rdm:Collection ,rdm:Project ,rdm:Resource ,rdm:SoftwareApplication                                             |
| definition@en | A Class which is published in this Class.                                                                      |
| definition@ja | 主語クラスをその一部として公開するクラス                                                                                           |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#ispreviousversionof |

| Property      | isReferencedBy                                                                                            |
|---------------|-----------------------------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/isReferencedBy                                                              |
| subPropertyOf | rdm:isRelatedTo                                                                                           |
| inverseOf     | rdm:references                                                                                            |
| domain        | rdm:Collection ,rdm:Project ,rdm:Resource ,rdm:SoftwareApplication                                        |
| range         | rdm:Collection ,rdm:Project ,rdm:Resource ,rdm:SoftwareApplication                                        |
| definition@en | A Class which uses this Class as a source of information.                                                 |
| definition@ja | 主語クラスを情報源として参照しているクラス                                                                                     |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#isreferencedby |

| Property      | isRequiredBy                                                                                            |
|---------------|---------------------------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/isRequiredBy                                                              |
| subPropertyOf | rdm:isRelatedTo                                                                                         |
| inverseOf     | rdm:requires                                                                                            |
| domain        | rdm:Resource ,rdm:SoftwareApplication                                                                   |
| range         | rdm:Resource ,rdm:SoftwareApplication                                                                   |
| definition@en | A Class which requires this Class.                                                                      |
| definition@ja | 主語クラスを必要とするクラス                                                                                          |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#isrequiredby |

| Property      | isReviewedBy                                                                                            |
|---------------|---------------------------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/isReviewedBy                                                              |
| subPropertyOf | rdm:isRelatedTo                                                                                         |
| inverseOf     | rdm:reviews                                                                                             |
| domain        | rdm:Resource ,rdm:SoftwareApplication                                                                   |
| range         | rdm:Review                                                                                              |
| definition@en | A Class which is a review of this Class.                                                                |
| definition@ja | 主語クラスのレビューとなっているクラス                                                                                     |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#isreviewedby |

| Property      | isSourceOf                                                                                            |
|---------------|-------------------------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/isSourceOf                                                              |
| subPropertyOf | rdm:isRelatedTo                                                                                       |
| domain        | rdm:Collection ,rdm:Project ,rdm:Resource                                                             |
| range         | rdm:Collection ,rdm:Project ,rdm:Resource                                                             |
| definition@en | A Class from which this Class is derived.                                                             |
| definition@ja | 主語クラスが基となっているクラス                                                                                      |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#issourceof |

| Property      | isSupplementTo                                                                                            |
|---------------|-----------------------------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/isSupplementTo                                                              |
| subPropertyOf | rdm:isRelatedTo                                                                                           |
| inverseOf     | rdm:isSupplementedBy                                                                                      |
| domain        | rdm:Collection ,rdm:Project ,rdm:Resource                                                                 |
| range         | rdm:Collection ,rdm:Project ,rdm:Resource                                                                 |
| definition@en | A Class that supplements this Class.                                                                      |
| definition@ja | 主語クラスが補足をしているクラス                                                                                          |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#issupplementto |

| Property      | isSupplementedBy                                                                                          |
|---------------|-----------------------------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/isSupplementedBy                                                            |
| subPropertyOf | rdm:isRelatedTo                                                                                           |
| domain        | rdm:Collection ,rdm:Project ,rdm:Resource                                                                 |
| range         | rdm:Collection ,rdm:Project ,rdm:Resource                                                                 |
| definition@en | A Class which is supplemented by this Class.                                                              |
| definition@ja | 主語クラスを補足しているクラス                                                                                           |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#issupplementby |

| Property      | isVariantFormOf                                                                                            |
|---------------|------------------------------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/isVariantFormOf                                                              |
| subPropertyOf | rdm:isRelatedTo                                                                                            |
| domain        | rdm:Resource ,rdm:SoftwareApplication                                                                      |
| range         | rdm:Resource ,rdm:SoftwareApplication                                                                      |
| definition@en | A Class which is the original form of this Class.                                                          |
| definition@ja | 主語クラスのオリジナルであるクラス                                                                                          |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#isvariantformof |

| Property      | isVersionOf                                                                                            |
|---------------|--------------------------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/isVersionOf                                                              |
| subPropertyOf | rdm:isRelatedTo                                                                                        |
| domain        | rdm:Collection ,rdm:Resource ,rdm:SoftwareApplication                                                  |
| range         | rdm:Collection ,rdm:Resource ,rdm:SoftwareApplication                                                  |
| definition@en | A Class  which this Class has as an another version.                                                   |
| definition@ja | 主語クラスが異なるバージョンであるクラス                                                                                   |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#isversionof |

| Property      | obsoletes                                                                                            |
|---------------|------------------------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/obsoletes                                                              |
| subPropertyOf | rdm:isRelatedTo                                                                                      |
| definition@en | A Class which is replaced by this Class.                                                             |
| definition@ja | 主語クラスによって置き換えられたクラス                                                                                  |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#obsoletes |

| Property      | references                                                                                            |
|---------------|-------------------------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/references                                                              |
| subPropertyOf | rdm:isRelatedTo                                                                                       |
| domain        | rdm:Collection ,rdm:Project ,rdm:Resource ,rdm:SoftwareApplication                                    |
| range         | rdm:Collection ,rdm:Project ,rdm:Resource ,rdm:SoftwareApplication                                    |
| definition@en | A Class which is used as a source of information by this Class.                                       |
| definition@ja | 主語クラスの情報源となったクラス                                                                                      |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#references |

| Property      | requires                                                                                            |
|---------------|-----------------------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/requires                                                              |
| subPropertyOf | rdm:isRelatedTo                                                                                     |
| domain        | rdm:Resource ,rdm:SoftwareApplication                                                               |
| range         | rdm:Resource ,rdm:SoftwareApplication                                                               |
| definition@en | A Class which is required by this Class.                                                            |
| definition@ja | 主語クラスを必要とするクラス                                                                                      |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#requires |

| Property      | reviews                                                                                            |
|---------------|----------------------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/reviews                                                              |
| subPropertyOf | rdm:isRelatedTo                                                                                    |
| domain        | rdm:Review                                                                                         |
| range         | rdm:Resource ,rdm:SoftwareApplication                                                              |
| definition@en | A Class which is reviewed by this Class.                                                           |
| definition@ja | 主語クラスによってレビューされたクラス                                                                                |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#reviews |

| Property      | isRequiredBy                                                                                            |
|---------------|---------------------------------------------------------------------------------------------------------|
| inverseOf     | rdm:requires                                                                                            |
| domain        | rdm:Resource ,rdm:SoftwareApplication                                                                   |
| range         | rdm:Resource ,rdm:SoftwareApplication                                                                   |
| definition@en | A Class which requires this Class.                                                                      |
| definition@ja | 主語クラスを必要とするクラス                                                                                          |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#isrequiredby |

| Property      | isReviewedBy                                                                                            |
|---------------|---------------------------------------------------------------------------------------------------------|
| inverseOf     | rdm:reviews                                                                                             |
| domain        | rdm:Resource ,rdm:SoftwareApplication                                                                   |
| range         | rdm:Review                                                                                              |
| definition@en | A Class which is a review of this Class.                                                                |
| definition@ja | 主語クラスのレビューとなっているクラス                                                                                     |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#isreviewedby |

| Property      | isSourceOf                                                                                            |
|---------------|-------------------------------------------------------------------------------------------------------|
| domain        | rdm:Collection ,rdm:Project ,rdm:Resource                                                             |
| range         | rdm:Collection ,rdm:Project ,rdm:Resource                                                             |
| definition@en | A Class from which this Class is derived.                                                             |
| definition@ja | 主語クラスが基となっているクラス                                                                                      |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#issourceof |

| Property      | isSupplementTo                                                                                            |
|---------------|-----------------------------------------------------------------------------------------------------------|
| inverseOf     | rdm:isSupplementedBy                                                                                      |
| domain        | rdm:Collection ,rdm:Project ,rdm:Resource                                                                 |
| range         | rdm:Collection ,rdm:Project ,rdm:Resource                                                                 |
| definition@en | A Class that supplements this Class.                                                                      |
| definition@ja | 主語クラスが補足をしているクラス                                                                                          |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#issupplementto |

| Property      | isSupplementedBy                                                                                          |
|---------------|-----------------------------------------------------------------------------------------------------------|
| domain        | rdm:Collection ,rdm:Project ,rdm:Resource                                                                 |
| range         | rdm:Collection ,rdm:Project ,rdm:Resource                                                                 |
| definition@en | A Class which is supplemented by this Class.                                                              |
| definition@ja | 主語クラスを補足しているクラス                                                                                           |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#issupplementby |

| Property      | isVariantFormOf                                                                                            |
|---------------|------------------------------------------------------------------------------------------------------------|
| domain        | rdm:Resource ,rdm:SoftwareApplication                                                                      |
| range         | rdm:Resource ,rdm:SoftwareApplication                                                                      |
| definition@en | A Class which is the original form of this Class.                                                          |
| definition@ja | 主語クラスのオリジナルであるクラス                                                                                          |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#isvariantformof |

| Property      | isVersionOf                                                                                            |
|---------------|--------------------------------------------------------------------------------------------------------|
| domain        | rdm:Collection ,rdm:Resource ,rdm:SoftwareApplication                                                  |
| range         | rdm:Collection ,rdm:Resource ,rdm:SoftwareApplication                                                  |
| definition@en | A Class  which this Class has as an another version.                                                   |
| definition@ja | 主語クラスが異なるバージョンであるクラス                                                                                   |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#isversionof |

| Property      | item                               |
|---------------|------------------------------------|
| IRI           | https://purl.org/rdm/ontology/item |
| range         | rdm:Resource                       |
| definition@en | A Resource related to this Class.  |
| definition@ja | 主語クラスと関連のあるリソース                    |

| Property      | collectionItem                               |
|---------------|----------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/collectionItem |
| subPropertyOf | rdm:item                                     |
| domain        | rdm:Collection                               |
| range         | rdm:Resource                                 |
| definition@en | A Resource included in this Collection.      |
| definition@ja | コレクションに含まれるリソース                              |

| Property      | dmpTargetItem                               |
|---------------|---------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/dmpTargetItem |
| subPropertyOf | rdm:item                                    |
| domain        | rdm:DataManagementPlan                      |
| range         | rdm:Resource                                |
| definition@en | A Resource described in DataManagementPlan. |
| definition@ja | DMPで対象になっているリソース                            |

| Property      | projectItem                               |
|---------------|-------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/projectItem |
| subPropertyOf | rdm:item                                  |
| domain        | rdm:Project                               |
| range         | rdm:Resource                              |
| definition@en | A Resource within this Project.           |
| definition@ja | プロジェクトに含まれるリソース                           |

| Property      | storedItem                               |
|---------------|------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/storedItem |
| subPropertyOf | rdm:item                                 |
| domain        | rdm:Repository                           |
| range         | rdm:Resource                             |
| definition@en | A Resource stored in this Repository.    |
| definition@ja | リポジトリに保存されている資源                          |

| Property      | licenseInformation                               |
|---------------|--------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/licenseInformation |
| domain        | rdm:Project ,rdm:Resource                        |
| range         | rdm:License                                      |
| definition@en | Information on license of this Class.            |
| definition@ja | プロジェクトやリソースのライセンス情報                              |

| Property      | dataLicenseInformation                                                   |
|---------------|--------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/dataLicenseInformation                     |
| subPropertyOf | rdm:licenseInformation                                                   |
| domain        | rdm:DataManagementPlan                                                   |
| definition@ja | DMPにおけるデータのライセンス                                                         |
| definition@en | The license of research data to be described in this DataManagementPlan. |

| Property      | material                                |
|---------------|-----------------------------------------|
| IRI           | https://purl.org/rdm/ontology/material  |
| domain        | rdm:Experiment                          |
| definition@en | Materials and inputs in the Experiment. |
| definition@ja | 実験における、材料や入力となるもの                       |

| Property      | obsoletes                                                                                            |
|---------------|------------------------------------------------------------------------------------------------------|
| definition@en | A Class which is replaced by this Class.                                                             |
| definition@ja | 主語クラスによって置き換えられたクラス                                                                                  |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#obsoletes |

| Property      | organizer                   |
|---------------|-----------------------------|
| domain        | rdm:Event                   |
| definition@en | An Event organizer or host. |
| definition@ja | イベントの開催者、主催者                |

| Property      | projectItem                     |
|---------------|---------------------------------|
| domain        | rdm:Project                     |
| range         | rdm:Resource                    |
| definition@en | A Resource within this Project. |
| definition@ja | プロジェクトに含まれるリソース                 |

| Property      | protocol                               |
|---------------|----------------------------------------|
| IRI           | https://purl.org/rdm/ontology/protocol |
| domain        | rdm:Experiment                         |
| definition@en | The protocol of this Experiment.       |
| definition@ja | 実験のプロトコル、手順                            |

| Property      | recipient                                                               |
|---------------|-------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/recipient                                 |
| domain        | rdm:Activity                                                            |
| range         | rdm:Person                                                              |
| definition@en | The recipient of this Activity and the affected party of this Activity. |
| definition@ja | 行動を受け取る・行動の影響を受ける相手                                                     |

| Property      | references                                                                                            |
|---------------|-------------------------------------------------------------------------------------------------------|
| domain        | rdm:Collection ,rdm:Project ,rdm:Resource ,rdm:SoftwareApplication                                    |
| range         | rdm:Collection ,rdm:Project ,rdm:Resource ,rdm:SoftwareApplication                                    |
| definition@en | A Class which is used as a source of information by this Class.                                       |
| definition@ja | 主語クラスの情報源となったクラス                                                                                      |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#references |

| Property      | requires                                                                                            |
|---------------|-----------------------------------------------------------------------------------------------------|
| domain        | rdm:Resource ,rdm:SoftwareApplication                                                               |
| range         | rdm:Resource ,rdm:SoftwareApplication                                                               |
| definition@en | A Class which is required by this Class.                                                            |
| definition@ja | 主語クラスを必要とするクラス                                                                                      |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#requires |

| Property      | researcher                             |
|---------------|----------------------------------------|
| domain        | rdm:Project                            |
| range         | rdm:Person                             |
| definition@en | A researcher involved in this Project. |
| definition@ja | プロジェクトに参加した研究者                         |

| Property      | result                                            |
|---------------|---------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/result              |
| inverseOf     | rdm:wasGeneratedBy                                |
| domain        | rdm:Activity ,rdm:Experiment                      |
| range         | rdm:Collection ,rdm:Project ,rdm:Resource         |
| definition@en | The result produced in this Activity /Experiment. |
| definition@ja | アクションや実験によって生成された新しいエンティティ                        |

| Property      | reviews                                                                                            |
|---------------|----------------------------------------------------------------------------------------------------|
| domain        | rdm:Review                                                                                         |
| range         | rdm:Resource ,rdm:SoftwareApplication                                                              |
| definition@en | A Class which is reviewed by this Class.                                                           |
| definition@ja | 主語クラスによってレビューされたクラス                                                                                |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#reviews |

| Property      | storedIn                                              |
|---------------|-------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/storedIn                |
| inverseOf     | rdm:storedItem                                        |
| domain        | rdm:Resource                                          |
| range         | rdm:Repository                                        |
| definition@en | Repository or storage where this Resource is managed. |
| definition@ja | リソースが管理されているリポジトリやストレージ                               |

| Property      | storedItem                            |
|---------------|---------------------------------------|
| domain        | rdm:Repository                        |
| range         | rdm:Resource                          |
| definition@en | A Resource stored in this Repository. |
| definition@ja | リポジトリに保存されている資源                       |

| Property      | target                                                                             |
|---------------|------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/target                                               |
| domain        | rdm:Activity                                                                       |
| range         | rdm:Collection ,rdm:Project ,rdm:Repository ,rdm:Resource ,rdm:SoftwareApplication |
| definition@en | The indirect object, or target, of this Activity.                                  |
| definition@ja | アクションの間接的な対象物                                                                      |

| Property      | fromLocation                               |
|---------------|--------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/fromLocation |
| subPropertyOf | rdm:target                                 |
| domain        | rdm:Download ,rdm:Upload                   |
| range         | rdm:Repository ,rdm:SoftwareApplication    |
| definition@en | Uploaded or downloaded from                |
| definition@ja | アップロードもしくはダウンロード元                          |

| Property      | toLocation                                           |
|---------------|------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/toLocation             |
| subPropertyOf | rdm:target                                           |
| domain        | rdm:Download ,rdm:Preserve ,rdm:Register ,rdm:Upload |
| range         | rdm:Repository ,rdm:SoftwareApplication              |
| definition@en | Upload or Download location                          |
| definition@ja | アップロードもしくはダウンロード先の場所                                 |

| Property      | thumbnail                               |
|---------------|-----------------------------------------|
| IRI           | https://purl.org/rdm/ontology/thumbnail |
| domain        | rdm:Resource                            |
| range         | rdm:Image                               |
| definition@en | A thumbnail of this Resource.           |
| definition@ja | サムネイル                                   |

| Property      | toLocation                                           |
|---------------|------------------------------------------------------|
| domain        | rdm:Download ,rdm:Preserve ,rdm:Register ,rdm:Upload |
| range         | rdm:Repository ,rdm:SoftwareApplication              |
| definition@en | Upload or Download location                          |
| definition@ja | アップロードもしくはダウンロード先の場所                                 |

| Property      | wasGeneratedBy                                             |
|---------------|------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/wasGeneratedBy               |
| domain        | rdm:Collection ,rdm:Project ,rdm:Resource                  |
| range         | rdm:Activity ,rdm:Experiment                               |
| definition@en | Activity or Experiment which created/generated this Class. |
| definition@ja | 主語クラスが生成されたアクションまたは実験                                      |

## Named Individual
# Usage Guidelines

There is two domain models of RDM Ontology; focused on Resource and focused on Activity. The former is focused on describing Resource as a outcome of research activities. The latter is focused on research activities itself. These two can be linked by using rdm property, however, it is not recommended because of the complexity.

## Domain Model Focused on Resource

![Resource domain model](../docs/domain_model_Resource.png)

To describe research outcomes such as research data, the main entity should be of type Resource. (It is recommended that a subclass of Resource be selected and used according to the category of research outcomes.) Related entities such as research project can be described by linking to the main entity. Activity entities is not recommended to add to this style of describing to divide the result of research activity (Resource) and the process (Activity).
Examples of Resource focused description is in two formats:

- [JSON-LD](../example/example_research_data.json)
- [turtle](../example/example_research_data.ttl)

## Domain Model Focused on Activity

![Resource domain model](../docs/domain_model_Activity.png)

To describe research activities as a log, the main entity should be a subclass of Activity class. Resource entities can be linked as a result, a target and a used tool of the activity. Linking other entities to Resource is not recommended when the main entity is subclass of Activity, as well as Resourced focused case.

# Term Definitions Overview

| prefix | Namespace                                   |
| ------ | ------------------------------------------- |
| rdm    | https://purl.org/rdm/ontology/              |
| owl    | http://www.w3.org/2002/07/owl#              |
| rdf    | http://www.w3.org/1999/02/22-rdf-syntax-ns# |
| rdfs   | http://www.w3.org/2000/01/rdf-schema#       |
| xsd    | http://www.w3.org/2001/XMLSchema#           |

## Class

### Base Class

| Class         | Activity                               |
| ------------- | -------------------------------------- |
| IRI           | https://purl.org/rdm/ontology/Activity |
| definition@en | An action or activity.                 |
| definition@en | 行動や行為                             |

| Class         | Actor                                                       |
| ------------- | ----------------------------------------------------------- |
| IRI           | https://purl.org/rdm/ontology/Actor                         |
| definition@en | Person or organization that is the subject of the Activity. |
| definition@en | Activity を行う主語にあたる人または組織                     |

| Class         | Object                                              |
| ------------- | --------------------------------------------------- |
| IRI           | https://purl.org/rdm/ontology/Object                |
| definition@en | Things and objects that are the object of Activity. |
| definition@en | Activity の目的語となる事物                         |

<!-- The following is generated automatically -->

### Activity

| Class         | Accept                                   |
|---------------|------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Accept     |
| definition@en | An act of approving Resource or request. |
| definition@ja | Resource や依頼を承認する行動                      |
| subClassOf    | rdm:Activity                             |

| Class         | Align                                 |
|---------------|---------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Align   |
| definition@en | An act of editing Resource to format. |
| definition@ja | Resource をフォーマットに合わせて編集する行動           |
| subClassOf    | rdm:Activity                          |

| Class         | Anonymize                               |
|---------------|-----------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Anonymize |
| definition@en | An act of making Resource anonymous.    |
| definition@ja | Resource を匿名化する行動                       |
| subClassOf    | rdm:Activity                            |

| Class         | Ask                                                |
|---------------|----------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Ask                  |
| definition@en | An act of asking questions to Person, chatbot etc. |
| definition@ja | Person やチャットボットなどに質問をする行動                          |
| subClassOf    | rdm:Activity                                       |

| Class         | Assign                                |
|---------------|---------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Assign  |
| definition@en | An act of assigning a role to Person. |
| definition@ja | Person に役割を任命する行動                     |
| subClassOf    | rdm:Activity                          |

| Class         | Authorize                                            |
|---------------|------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Authorize              |
| definition@en | An act of granting permission or right to an object. |
| definition@ja | 権利や許可を与える行動                                          |
| subClassOf    | rdm:Activity                                         |

| Class         | Check                                                                     |
|---------------|---------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Check                                       |
| definition@en | An act of checking the regulation for Resource, such as using checkboxes. |
| definition@ja | チェックボックスに印をつけるなど、規定の項目に関して確認する行動                                          |
| subClassOf    | rdm:Activity                                                              |

| Class         | Cleanse                                          |
|---------------|--------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Cleanse            |
| definition@en | An act of performing data cleansing of Resource. |
| definition@ja | Resource をデータクレンジングする行動                          |
| subClassOf    | rdm:Activity                                     |

| Class         | Collect                               |
|---------------|---------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Collect |
| definition@en | An act of collecting Resource.        |
| definition@ja | Resource を収集する行動                      |
| subClassOf    | rdm:Activity                          |

| Class         | Comment                                     |
|---------------|---------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Comment       |
| definition@en | An act of generating a comment on Resource. |
| definition@ja | Resource に対してコメントをする行動                      |
| subClassOf    | rdm:Activity                                |

| Class         | Connect                                          |
|---------------|--------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Connect            |
| definition@en | An act of connecting service to another service. |
| definition@ja | サービスを別のサービスに接続する行動                               |
| subClassOf    | rdm:Activity                                     |

| Class         | Convert                                            |
|---------------|----------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Convert              |
| definition@en | An act of converting Resource into a new Resource. |
| definition@ja | Resource を新たな Resource に変換する行動                     |
| subClassOf    | rdm:Activity                                       |

| Class         | Create                                                                     |
|---------------|----------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Create                                       |
| definition@en | An act of creating/producing/generating Resource, Project, Collection etc. |
| definition@ja | Project, Resource, Collection などを作成する行動                                    |
| subClassOf    | rdm:Activity                                                               |

| Class         | Dump                                      |
|---------------|-------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Dump        |
| definition@en | An act of creating a log file by dumping. |
| definition@ja | ダンプによりログファイルを作成する行動                       |
| subClassOf    | rdm:Create                                |

| Class         | Deploy                                               |
|---------------|------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Deploy                 |
| definition@en | An act of deploying SoftwareApplication or Resource. |
| definition@ja | Resource, SoftwareApplicationをデプロイする行動               |
| subClassOf    | rdm:Activity                                         |

| Class         | Develop                               |
|---------------|---------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Develop |
| definition@en | An act of developing a program.       |
| definition@ja | プログラミングで実装する行動                        |
| subClassOf    | rdm:Activity                          |

| Class         | Download                               |
|---------------|----------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Download |
| definition@en | An act of downloading Resource.        |
| definition@ja | Resource をダウンロードする行動                   |
| subClassOf    | rdm:Activity                           |

| Class         | Evaluate                                            |
|---------------|-----------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Evaluate              |
| definition@en | An act of evaluating Resource, such as peer-review. |
| definition@ja | ピアレビューなど、Resource を評価する行動                           |
| subClassOf    | rdm:Activity                                        |

| Class         | Execute                                                         |
|---------------|-----------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Execute                           |
| definition@en | An act of executing SoftwareApplication, Resource, program etc. |
| definition@ja | Resource, SoftwareApplication, プログラムを実行する行動                     |
| subClassOf    | rdm:Activity                                                    |

| Class         | Get                                                    |
|---------------|--------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Get                      |
| definition@en | An act of getting/obtaining Resource, information etc. |
| definition@ja | Resource または情報などを取得する行動                                |
| subClassOf    | rdm:Activity                                           |

| Class         | Inform                                                 |
|---------------|--------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Inform                   |
| definition@en | An act of notifying Person/Institution of information. |
| definition@ja | Person, Institution に対して通知する行動                         |
| subClassOf    | rdm:Activity                                           |

| Class         | Ingest                                                                                              |
|---------------|-----------------------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Ingest                                                                |
| definition@en | An act of getting and adding metadata to Resource from public information as part of data curation. |
| definition@ja | キュレーションの一環として、Resource のメタデータを外部から取得し付与する行動                                                         |
| subClassOf    | rdm:Activity                                                                                        |

| Class         | Integrate                                                                   |
|---------------|-----------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Integrate                                     |
| definition@en | An act of integrating different forms of metadata as part of data curation. |
| definition@ja | キュレーションの一環として、メタデータを統合する行動                                                  |
| subClassOf    | rdm:Activity                                                                |

| Class         | Preserve                                                                      |
|---------------|-------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Preserve                                        |
| definition@en | An act of saving and storing Resource to Repository, SoftwareApplication etc. |
| definition@ja | Resource を Repository, SoftwareApplication などに保存・保管する行動                       |
| subClassOf    | rdm:Activity                                                                  |

| Class         | Archive                               |
|---------------|---------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Archive |
| definition@en | An act of archiving Resource.         |
| definition@ja | Resource をアーカイブする行動                   |
| subClassOf    | rdm:Preserve                          |

| Class         | Publish                                                                                                                                |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Publish                                                                                                  |
| definition@en | An act of making Resource public, such as by pushing "publish" button on publishing service. (including Resource of any access rights) |
| definition@ja | 公開ボタンを押すなどして、Resource を公開する行動(アクセス権の種類は問わない)                                                                                           |
| subClassOf    | rdm:Activity                                                                                                                           |

| Class         | Register                                                                            |
|---------------|-------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Register                                              |
| definition@en | An act of registering Resource to Repository, SoftwareApplication or other service. |
| definition@ja | Repository, SoftwareApplication もしくはその他サービスに、 Resource を登録する行動                      |
| subClassOf    | rdm:Activity                                                                        |

| Class         | Reject                                                             |
|---------------|--------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Reject                               |
| definition@en | An act of rejecting proposal/assigned role/submitted Resource etc. |
| definition@ja | 提出された Resource や提案、割り当てられた役割などを取り下げる行動                             |
| subClassOf    | rdm:Activity                                                       |

| Class         | Rename                               |
|---------------|--------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Rename |
| definition@en | An act of renaming Resource.         |
| definition@ja | Resource の名称を変更する行動                  |
| subClassOf    | rdm:Activity                         |

| Class         | Reorganize                                      |
|---------------|-------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Reorganize        |
| definition@en | An act of changing folder structure of Dataset. |
| definition@ja | Dataset のフォルダ構成を変更する行動                          |
| subClassOf    | rdm:Activity                                    |

| Class         | Restructure                                                                          |
|---------------|--------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Restructure                                            |
| definition@en | An act of re-structuring Resource as part of data curation, such as sorting a table. |
| definition@ja | 表データをソートするなど、キュレーションの一環として Resource を再構成する行動                                         |
| subClassOf    | rdm:Activity                                                                         |

| Class         | Schedule                               |
|---------------|----------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Schedule |
| definition@en | An act of scheduling future Event.     |
| definition@ja | 未来に行われる Event を設定する行動                  |
| subClassOf    | rdm:Activity                           |

| Class         | Search                                                            |
|---------------|-------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Search                              |
| definition@en | An act of searching Resource, such as by pushing "search" button. |
| definition@ja | 検索ボタンの押下など、Resource を検索する行動                                       |
| subClassOf    | rdm:Activity                                                      |

| Class         | Select                               |
|---------------|--------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Select |
| definition@en | An act of selecting from options.    |
| definition@ja | 選択肢の中から利用するものを選択する行動                 |
| subClassOf    | rdm:Activity                         |

| Class         | Send                               |
|---------------|------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Send |
| definition@en | An act of dispatching Resource.    |
| definition@ja | Resource を送る行動                     |
| subClassOf    | rdm:Activity                       |

| Class         | Suggest                                    |
|---------------|--------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Suggest      |
| definition@en | An act of presenting or proposing options. |
| definition@ja | 選択肢を提示する行動                                 |
| subClassOf    | rdm:Activity                               |

| Class         | Update                                                |
|---------------|-------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Update                  |
| definition@en | An act of updating an existing Resource with changes. |
| definition@ja | 既存の Resource に変更を加え更新する行動                             |
| subClassOf    | rdm:Activity                                          |

| Class         | Upload                                                               |
|---------------|----------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Upload                                 |
| definition@en | An act of uploading Resource to Repository, SoftwareApplication etc. |
| definition@ja | Resource を SoftwareApplicationやRepository 等にアップロードする行動               |
| subClassOf    | rdm:Activity                                                         |

| Class         | Visualize                                                                 |
|---------------|---------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Visualize                                   |
| definition@en | An act of creating a visualization based on data, such as making a graph. |
| definition@ja | グラフを生成するなど、データを元に可視化する行動                                                  |
| subClassOf    | rdm:Activity                                                              |

### Actor

| Class         | Institution                               |
|---------------|-------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Institution |
| definition@en | An organization.                          |
| definition@ja | 機関や組織                                     |
| subClassOf    | rdm:Actor                                 |

| Class         | FundingAgency                                   |
|---------------|-------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/FundingAgency     |
| definition@en | An organization that funds research activities. |
| definition@ja | 研究資金提供機関                                        |
| subClassOf    | rdm:Institution                                 |

| Class         | Person                               |
|---------------|--------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Person |
| definition@en | A person.                            |
| definition@ja | 人物                                   |
| subClassOf    | rdm:Actor                            |

### Object

| Class         | Collection                               |
|---------------|------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Collection |
| definition@en | A collection of items.                   |
| definition@ja | オブジェクトのコレクション                            |
| subClassOf    | rdm:Object                               |

| Class         | DataManagementPlan                               |
|---------------|--------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/DataManagementPlan |
| definition@en | A data management plan (DMP).                    |
| definition@ja | データ管理計画(DMP)                                     |
| subClassOf    | rdm:Object                                       |

| Class         | Event                               |
|---------------|-------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Event |
| definition@en | An event, such as conferences etc.  |
| definition@ja | 学会など、イベントや催し物                       |
| subClassOf    | rdm:Object                          |

| Class         | Experiment                               |
|---------------|------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Experiment |
| definition@en | Experiment                               |
| definition@ja | 実験                                       |
| subClassOf    | rdm:Object                               |

| Class         | Grant                               |
|---------------|-------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Grant |
| definition@en | A grant for research activities.    |
| definition@ja | 研究資金プログラム                           |
| subClassOf    | rdm:Object                          |

| Class         | Identifier                               |
|---------------|------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Identifier |
| definition@en | An identifier.                           |
| definition@ja | 識別子                                      |
| subClassOf    | rdm:Object                               |

| Class         | Intangible                                    |
|---------------|-----------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Intangible      |
| definition@en | Abstract class for concepts without entities. |
| definition@ja | 実体を伴わない概念のための抽象クラス                            |
| subClassOf    | rdm:Object                                    |

| Class         | Role                               |
|---------------|------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Role |
| definition@en | Roles and positions.               |
| definition@ja | 役割、役職                              |
| subClassOf    | rdm:Intangible                     |

| Class         | Project                               |
|---------------|---------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Project |
| definition@en | A research project.                   |
| definition@ja | 研究プロジェクト                              |
| subClassOf    | rdm:Object                            |

| Class         | Repository                               |
|---------------|------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Repository |
| definition@en | A repository.                            |
| definition@ja | リポジトリ                                    |
| subClassOf    | rdm:Object                               |

| Class         | Resource                                                           |
|---------------|--------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Resource                             |
| definition@en | A digital object, such as research data, video of experiments rtc. |
| definition@ja | 研究データや実験動画など、デジタルオブジェクト                                            |
| subClassOf    | rdm:Object                                                         |

| Class         | Audio                               |
|---------------|-------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Audio |
| definition@en | An audio file.                      |
| definition@ja | 音声                                  |
| subClassOf    | rdm:Resource                        |

| Class         | Book                               |
|---------------|------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Book |
| definition@en | A book.                            |
| definition@ja | 書籍                                 |
| subClassOf    | rdm:Resource                       |

| Class         | ConferenceObject                               |
|---------------|------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/ConferenceObject |
| definition@en | A Resource related to conferences.             |
| definition@ja | カンファレンスに関連するリソース                               |
| subClassOf    | rdm:Resource                                   |

| Class         | ConferencePaper                               |
|---------------|-----------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/ConferencePaper |
| definition@en | A conference paper.                           |
| definition@ja | カンファレンスペーパー                                   |
| subClassOf    | rdm:Resource                                  |

| Class         | ConferenceProceeding                               |
|---------------|----------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/ConferenceProceeding |
| definition@en | A conference proceeding.                           |
| definition@ja | カンファレンスプロシーディング                                    |
| subClassOf    | rdm:Resource                                       |

| Class         | Dataset                               |
|---------------|---------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Dataset |
| definition@en | A dataset.                            |
| definition@ja | データセット                                |
| subClassOf    | rdm:Resource                          |

| Class         | EducationalResource                                            |
|---------------|----------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/EducationalResource              |
| definition@en | A Resource related to educational, such as slides for lecture. |
| definition@ja | 教育関連資料                                                         |
| subClassOf    | rdm:Resource                                                   |

| Class         | Image                               |
|---------------|-------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Image |
| definition@en | An image file.                      |
| definition@ja | 画像                                  |
| subClassOf    | rdm:Resource                        |

| Class         | Journal                               |
|---------------|---------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Journal |
| definition@en | A journal.                            |
| definition@ja | ジャーナル                                 |
| subClassOf    | rdm:Resource                          |

| Class         | JournalArticle                               |
|---------------|----------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/JournalArticle |
| definition@en | An article published in a journal.           |
| definition@ja | ジャーナル論文                                      |
| subClassOf    | rdm:Resource                                 |

| Class         | Message                               |
|---------------|---------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Message |
| definition@en | Message and comment.                  |
| definition@ja | メッセージやコメント                            |
| subClassOf    | rdm:Resource                          |

| Class         | MetadataDocument                               |
|---------------|------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/MetadataDocument |
| definition@en | Metadata of any Resource.                      |
| definition@ja | Resource に関するメタデータ                             |
| subClassOf    | rdm:Resource                                   |

| Class         | OtherResource                               |
|---------------|---------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/OtherResource |
| definition@en | An other Resource.                          |
| definition@ja | その他のリソース                                    |
| subClassOf    | rdm:Resource                                |

| Class         | Preprint                               |
|---------------|----------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Preprint |
| definition@en | A preprint.                            |
| definition@ja | プレプリント                                 |
| subClassOf    | rdm:Resource                           |

| Class         | Report                               |
|---------------|--------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Report |
| definition@en | A report.                            |
| definition@ja | レポート、報告書                             |
| subClassOf    | rdm:Resource                         |

| Class         | Review                               |
|---------------|--------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Review |
| definition@en | Review documents and evaluations.    |
| definition@ja | レビュー文書や評価                            |
| subClassOf    | rdm:Resource                         |

| Class         | Standard                               |
|---------------|----------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Standard |
| definition@en | A standard.                            |
| definition@ja | 標準                                     |
| subClassOf    | rdm:Resource                           |

| Class         | Thesis                               |
|---------------|--------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Thesis |
| definition@en | A thesis.                            |
| definition@ja | 学位論文                                 |
| subClassOf    | rdm:Resource                         |

| Class         | Video                               |
|---------------|-------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Video |
| definition@en | A video file.                       |
| definition@ja | 動画                                  |
| subClassOf    | rdm:Resource                        |

| Class         | Workflow                               |
|---------------|----------------------------------------|
| IRI           | https://purl.org/rdm/ontology/Workflow |
| definition@en | A workflow.                            |
| definition@ja | ワークフロー                                 |
| subClassOf    | rdm:Resource                           |

| Class         | RightsStatement                                     |
|---------------|-----------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/RightsStatement       |
| definition@en | A higer-level class that relates to various rights. |
| definition@ja | 権利関係全般に関連するクラス                                      |
| subClassOf    | rdm:Object                                          |

| Class         | AccessRights                               |
|---------------|--------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/AccessRights |
| definition@en | An access right o Resource.                |
| definition@ja | リソースへのアクセス権                                |
| subClassOf    | rdm:RightsStatement                        |

| Class         | License                               |
|---------------|---------------------------------------|
| IRI           | https://purl.org/rdm/ontology/License |
| definition@en | A license of Resource.                |
| definition@ja | リソースのライセンス                            |
| subClassOf    | rdm:RightsStatement                   |

| Class         | SoftwareApplication                               |
|---------------|---------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/SoftwareApplication |
| definition@en | A software application.                           |
| definition@ja | ソフトウェアアプリケーション                                    |
| subClassOf    | rdm:Object                                        |
## Property

### Datatype Property

| Property      | additionalName                                       |
|---------------|------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/additionalName         |
| domain        | rdm:Person                                           |
| definition@en | An additional name for this Person e.g. middle name. |
| definition@ja | ミドルネームなど、その他の名前                                      |

| Property      | address                               |
|---------------|---------------------------------------|
| IRI           | https://purl.org/rdm/ontology/address |
| domain        | rdm:Institution                       |
| range         | xsd:string                            |
| definition@en | Address of this Institution.          |
| definition@ja | 研究機関の住所                               |

| Property      | approximateSize                                                               |
|---------------|-------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/approximateSize                                 |
| domain        | rdm:DataManagementPlan                                                        |
| range         | xsd:string                                                                    |
| definition@en | Approximate size of research data to be described in this DataManagementPlan. |
| definition@ja | DMPにおける概略データ量                                                                 |

| Property      | collectionSize                               |
|---------------|----------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/collectionSize |
| domain        | rdm:Collection                               |
| range         | xsd:nonNegativeInteger                       |
| definition@en | The number of items in this Collection.      |
| definition@ja | 所定のパッケージに含まれるデータセットの総数                       |

| Property      | contact                                                                                             |
|---------------|-----------------------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/contact                                                               |
| domain        | rdm:DataManagementPlan                                                                              |
| range         | xsd:string                                                                                          |
| definition@en | Contacts for data management organizations and managers to be described in this DataManagementPlan. |
| definition@ja | DMPにおけるデータ管理機関・管理者への連絡先                                                                             |

| Property      | copyright                               |
|---------------|-----------------------------------------|
| IRI           | https://purl.org/rdm/ontology/copyright |
| domain        | rdm:License                             |
| range         | xsd:string                              |
| definition@en | A copyright notice.                     |
| definition@ja | コピーライト表記                                |

| Property      | dataAccessRequirements                                                     |
|---------------|----------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/dataAccessRequirements                       |
| domain        | rdm:AccessRights                                                           |
| range         | xsd:string                                                                 |
| definition@en | Conditions and method of access to the Resource under access restrictions. |
| definition@ja | アクセス権が限定公開の場合のアクセス条件と方法                                                    |

| Property      | dataDescription                                                              |
|---------------|------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/dataDescription                                |
| domain        | rdm:DataManagementPlan                                                       |
| definition@ja | DMPにおけるデータの説明                                                                |
| definition@en | The description of research data to be described in this DataManagementPlan. |

| Property      | dataEncodingFormat                                                      |
|---------------|-------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/dataEncodingFormat                        |
| domain        | rdm:DataManagementPlan                                                  |
| definition@ja | DMPで記述した研究データのフォーマット                                                    |
| definition@en | The format of research data to be described in this DataManagementPlan. |

| Property      | dataNumber                                           |
|---------------|------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/dataNumber             |
| domain        | rdm:DataManagementPlan                               |
| range         | xsd:nonNegativeInteger                               |
| definition@ja | DMPにおけるデータNo.                                        |
| definition@en | The data number assigned to this DataManagementPlan. |

| Property      | date                               |
|---------------|------------------------------------|
| IRI           | https://purl.org/rdm/ontology/date |
| range         | xsd:date ,xsd:dateTime             |
| definition@en | A date or datetime.                |
| definition@ja | 日付または日時                            |

| Property      | dateAvailable                                                                       |
|---------------|-------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/dateAvailable                                         |
| subPropertyOf | rdm:date                                                                            |
| domain        | rdm:AccessRights                                                                    |
| definition@en | Scheduled date of open access of the Resource under the rights of embargoed access. |
| definition@ja | 公開猶予の場合の公開予定日                                                                       |

| Property      | dateCreated                                  |
|---------------|----------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/dateCreated    |
| subPropertyOf | rdm:date                                     |
| domain        | rdm:Resource                                 |
| definition@en | The date on which this Resource was created. |
| definition@ja | リソースの作成日                                     |

| Property      | dateEnded                                      |
|---------------|------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/dateEnded        |
| subPropertyOf | rdm:date                                       |
| domain        | rdm:Activity ,rdm:Event ,rdm:Project ,rdm:Role |
| definition@en | The end date of this Class.                    |
| definition@ja | クラスの終了日                                        |

| Property      | dateModified                                               |
|---------------|------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/dateModified                 |
| subPropertyOf | rdm:date                                                   |
| domain        | rdm:Resource                                               |
| definition@en | The date on which the Resource was most recently modified. |
| definition@ja | リソースの最終更新日                                                 |

| Property      | datePublished                                  |
|---------------|------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/datePublished    |
| subPropertyOf | rdm:date                                       |
| domain        | rdm:Resource                                   |
| definition@en | The date on which this Resource was published. |
| definition@ja | リソースの発行日・公開日                                   |

| Property      | dateStarted                                    |
|---------------|------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/dateStarted      |
| subPropertyOf | rdm:date                                       |
| domain        | rdm:Activity ,rdm:Event ,rdm:Project ,rdm:Role |
| definition@en | The start date of this Class.                  |
| definition@ja | クラスの開始日                                        |

| Property      | dateUpdated                                                         |
|---------------|---------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/dateUpdated                           |
| subPropertyOf | rdm:date                                                            |
| domain        | rdm:Event                                                           |
| definition@en | The date on which this Event information was most recently updated. |
| definition@ja | イベントの内容更新日                                                          |

| Property      | sdDatePublished                               |
|---------------|-----------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/sdDatePublished |
| subPropertyOf | rdm:date                                      |
| domain        | rdm:Resource                                  |
| definition@en | The acquisition date of this Resource.        |
| definition@ja | 外部ファイルの取得日                                    |

| Property      | dateAvailable                                                                       |
|---------------|-------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/dateAvailable                                         |
| domain        | rdm:AccessRights                                                                    |
| definition@en | Scheduled date of open access of the Resource under the rights of embargoed access. |
| definition@ja | 公開猶予の場合の公開予定日                                                                       |

| Property      | dateCreated                                  |
|---------------|----------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/dateCreated    |
| domain        | rdm:Resource                                 |
| definition@en | The date on which this Resource was created. |
| definition@ja | リソースの作成日                                     |

| Property      | dateEnded                                      |
|---------------|------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/dateEnded        |
| domain        | rdm:Activity ,rdm:Event ,rdm:Project ,rdm:Role |
| definition@en | The end date of this Class.                    |
| definition@ja | クラスの終了日                                        |

| Property      | dateModified                                               |
|---------------|------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/dateModified                 |
| domain        | rdm:Resource                                               |
| definition@en | The date on which the Resource was most recently modified. |
| definition@ja | リソースの最終更新日                                                 |

| Property      | datePublished                                  |
|---------------|------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/datePublished    |
| domain        | rdm:Resource                                   |
| definition@en | The date on which this Resource was published. |
| definition@ja | リソースの発行日・公開日                                   |

| Property      | dateStarted                                    |
|---------------|------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/dateStarted      |
| domain        | rdm:Activity ,rdm:Event ,rdm:Project ,rdm:Role |
| definition@en | The start date of this Class.                  |
| definition@ja | クラスの開始日                                        |

| Property      | dateUpdated                                                         |
|---------------|---------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/dateUpdated                           |
| domain        | rdm:Event                                                           |
| definition@en | The date on which this Event information was most recently updated. |
| definition@ja | イベントの内容更新日                                                          |

| Property      | description                                                                    |
|---------------|--------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/description                                      |
| domain        | rdm:Experiment ,rdm:Grant ,rdm:Project ,rdm:Repository ,rdm:Resource ,rdm:Role |
| range         | xsd:string                                                                     |
| definition@en | A description of this Class.                                                   |
| definition@ja | クラスの説明                                                                         |

| Property      | dataAccessRequirements                                                     |
|---------------|----------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/dataAccessRequirements                       |
| subPropertyOf | rdm:description                                                            |
| domain        | rdm:AccessRights                                                           |
| range         | xsd:string                                                                 |
| definition@en | Conditions and method of access to the Resource under access restrictions. |
| definition@ja | アクセス権が限定公開の場合のアクセス条件と方法                                                    |

| Property      | dataDescription                                                              |
|---------------|------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/dataDescription                                |
| subPropertyOf | rdm:description                                                              |
| domain        | rdm:DataManagementPlan                                                       |
| definition@ja | DMPにおけるデータの説明                                                                |
| definition@en | The description of research data to be described in this DataManagementPlan. |

| Property      | measurementTechnique                                            |
|---------------|-----------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/measurementTechnique              |
| subPropertyOf | rdm:description                                                 |
| domain        | rdm:DataManagementPlan                                          |
| range         | xsd:string                                                      |
| definition@en | A technique, method or technology used to create research data. |
| definition@ja | 研究データの収集・取得方法                                                   |

| Property      | operatingSystem                                          |
|---------------|----------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/operatingSystem            |
| subPropertyOf | rdm:description                                          |
| domain        | rdm:SoftwareApplication                                  |
| range         | xsd:string                                               |
| definition@en | Operating systems supported by this SoftwareApplication. |
| definition@ja | アプリケーションがサポートされているOS                                     |

| Property      | processorRequirements                                            |
|---------------|------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/processorRequirements              |
| subPropertyOf | rdm:description                                                  |
| domain        | rdm:SoftwareApplication                                          |
| range         | xsd:string                                                       |
| definition@en | Processor architecture required to run this SoftwareApplication. |
| definition@ja | アプリケーション実行に必要なプロセッサー要件                                           |

| Property      | protocolText                               |
|---------------|--------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/protocolText |
| subPropertyOf | rdm:description                            |
| domain        | rdm:Experiment                             |
| definition@en | A text of protocol of this Experiment.     |
| definition@ja | 実験のプロトコル、手順を示したテキスト                        |

| Property      | purpose                                                                               |
|---------------|---------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/purpose                                                 |
| subPropertyOf | rdm:description                                                                       |
| domain        | rdm:Event                                                                             |
| range         | xsd:string                                                                            |
| definition@en | Context of this Event implementation e.g. reasons and backgrounds for implementation. |
| definition@ja | 実施に至った理由や背景など、イベント実施のコンテクスト                                                           |

| Property      | readme                                                     |
|---------------|------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/readme                       |
| subPropertyOf | rdm:description                                            |
| domain        | rdm:SoftwareApplication                                    |
| definition@en | A text description as Read Me of this SoftwareApplication. |
| definition@ja | README                                                     |

| Property      | softwareRequirements                                            |
|---------------|-----------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/softwareRequirements              |
| subPropertyOf | rdm:description                                                 |
| domain        | rdm:SoftwareApplication                                         |
| range         | xsd:string                                                      |
| definition@en | Component dependency requirements for this SoftwareApplication. |
| definition@ja | アプリケーションコンポーネントの依存要件                                            |

| Property      | specialRequirements                               |
|---------------|---------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/specialRequirements |
| subPropertyOf | rdm:description                                   |
| domain        | rdm:SoftwareApplication                           |
| range         | xsd:string                                        |
| definition@en | Other requirements for this SoftwareApplication.  |
| definition@ja | 他のプロパティに当てはまらないアプリケーションに必要な条件                     |

| Property      | storageRequirements                               |
|---------------|---------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/storageRequirements |
| subPropertyOf | rdm:description                                   |
| domain        | rdm:SoftwareApplication                           |
| range         | xsd:string                                        |
| definition@en | Storage requirements.                             |
| definition@ja | ストレージの要件                                          |

| Property      | detailedRole                               |
|---------------|--------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/detailedRole |
| domain        | rdm:Person                                 |
| range         | xsd:string                                 |
| definition@en | A detailed role of this Person.            |
| definition@ja | 詳細な役割                                      |

| Property      | detailedType                               |
|---------------|--------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/detailedType |
| domain        | rdm:Resource                               |
| range         | xsd:string                                 |
| definition@en | A detailed type of this Resource.          |
| definition@ja | 詳細な資源タイプ                                   |

| Property      | dmpFormat                               |
|---------------|-----------------------------------------|
| IRI           | https://purl.org/rdm/ontology/dmpFormat |
| domain        | rdm:DataManagementPlan                  |
| range         | xsd:string                              |
| definition@en | A name of DataManagementPlan format.    |
| definition@ja | DMP種別名                                  |

| Property      | doi                               |
|---------------|-----------------------------------|
| IRI           | https://purl.org/rdm/ontology/doi |
| domain        | rdm:Project ,rdm:Resource         |
| range         | xsd:anyURI                        |
| definition@ja | DOI                               |
| definition@en | DOI URL.                          |
| seeAlso       | https://www.doi.org/              |

| Property      | email                               |
|---------------|-------------------------------------|
| IRI           | https://purl.org/rdm/ontology/email |
| domain        | rdm:Person                          |
| range         | xsd:string                          |
| definition@en | Email address.                      |
| definition@ja | メールアドレス                             |

| Property      | encodingFormat                               |
|---------------|----------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/encodingFormat |
| domain        | rdm:Resource                                 |
| range         | xsd:string                                   |
| definition@en | A MIME format of this Resource.              |
| definition@ja | リソースのフォーマット                                  |
| seeAlso       | http://www.iana.org/assignments/media-types/ |

| Property      | dataEncodingFormat                                                      |
|---------------|-------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/dataEncodingFormat                        |
| subPropertyOf | rdm:encodingFormat                                                      |
| domain        | rdm:DataManagementPlan                                                  |
| definition@ja | DMPで記述した研究データのフォーマット                                                    |
| definition@en | The format of research data to be described in this DataManagementPlan. |

| Property      | eradResearcherNumber                               |
|---------------|----------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/eradResearcherNumber |
| domain        | rdm:Person                                         |
| range         | xsd:string                                         |
| definition@en | e-rad researcher number.                           |
| definition@ja | e-rad 研究者番号                                        |
| seeAlso       | https://www.e-rad.go.jp/                           |

| Property      | familyName                               |
|---------------|------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/familyName |
| domain        | rdm:Person                               |
| definition@en | Family name.                             |
| definition@ja | 名字                                       |

| Property      | field                                      |
|---------------|--------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/field        |
| domain        | rdm:Project ,rdm:Resource                  |
| range         |                                            |
| definition@en | A research field of this Project/Resource. |
| definition@ja | プロジェクト・リソースの主題                             |

| Property      | funderId                                           |
|---------------|----------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/funderId             |
| domain        | rdm:FundingAgency                                  |
| range         | xsd:string                                         |
| definition@en | Funder ID.                                         |
| definition@ja | 助成機関識別子                                            |
| seeAlso       | https://www.crossref.org/services/funder-registry/ |

| Property      | givenName                               |
|---------------|-----------------------------------------|
| IRI           | https://purl.org/rdm/ontology/givenName |
| domain        | rdm:Person                              |
| definition@en | Given name.                             |
| definition@ja | ファーストネーム                                |

| Property      | hashValue                               |
|---------------|-----------------------------------------|
| IRI           | https://purl.org/rdm/ontology/hashValue |
| domain        | rdm:Resource                            |
| range         | xsd:string                              |
| definition@en | Hash value.                             |
| definition@ja | ハッシュ値                                   |

| Property      | sha256                               |
|---------------|--------------------------------------|
| IRI           | https://purl.org/rdm/ontology/sha256 |
| subPropertyOf | rdm:hashValue                        |
| domain        | rdm:Resource                         |
| range         | xsd:string                           |
| definition@en | sha256 hash value.                   |
| definition@ja | sha256のハッシュ値                         |

| Property      | identifierName                               |
|---------------|----------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/identifierName |
| domain        | rdm:Identifier                               |
| definition@en | A name of identifier scheme e.g. DOI.        |
| definition@ja | 識別子のスキーマ名                                    |

| Property      | identifierValue                               |
|---------------|-----------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/identifierValue |
| domain        | rdm:Identifier                                |
| range         | xsd:anyURI ,xsd:string                        |
| definition@en | Identifier value.                             |
| definition@ja | 識別子の値                                         |

| Property      | doi                               |
|---------------|-----------------------------------|
| IRI           | https://purl.org/rdm/ontology/doi |
| subPropertyOf | rdm:identifierValue               |
| domain        | rdm:Project ,rdm:Resource         |
| range         | xsd:anyURI                        |
| definition@ja | DOI                               |
| definition@en | DOI URL.                          |
| seeAlso       | https://www.doi.org/              |

| Property      | eradResearcherNumber                               |
|---------------|----------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/eradResearcherNumber |
| subPropertyOf | rdm:identifierValue                                |
| domain        | rdm:Person                                         |
| range         | xsd:string                                         |
| definition@en | e-rad researcher number.                           |
| definition@ja | e-rad 研究者番号                                        |
| seeAlso       | https://www.e-rad.go.jp/                           |

| Property      | funderId                                           |
|---------------|----------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/funderId             |
| subPropertyOf | rdm:identifierValue                                |
| domain        | rdm:FundingAgency                                  |
| range         | xsd:string                                         |
| definition@en | Funder ID.                                         |
| definition@ja | 助成機関識別子                                            |
| seeAlso       | https://www.crossref.org/services/funder-registry/ |

| Property      | isbn                               |
|---------------|------------------------------------|
| IRI           | https://purl.org/rdm/ontology/isbn |
| subPropertyOf | rdm:identifierValue                |
| domain        | rdm:Book                           |
| range         | xsd:string                         |
| definition@en | ISBN code.                         |
| definition@ja | ISBNコード                            |

| Property      | japanGrantNumber                               |
|---------------|------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/japanGrantNumber |
| subPropertyOf | rdm:identifierValue                            |
| domain        | rdm:Grant                                      |
| range         | xsd:string                                     |
| definition@en | Japan grant number.                            |
| definition@ja | 体系的課題番号                                        |
| seeAlso       | https://www.nistep.go.jp/archives/53002        |

| Property      | localIdentifier                               |
|---------------|-----------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/localIdentifier |
| subPropertyOf | rdm:identifierValue                           |
| domain        | rdm:Experiment ,rdm:Resource                  |
| definition@en | Local identifier.                             |
| definition@ja | ローカル識別子                                       |

| Property      | orcid                               |
|---------------|-------------------------------------|
| IRI           | https://purl.org/rdm/ontology/orcid |
| subPropertyOf | rdm:identifierValue                 |
| domain        | rdm:Person                          |
| range         | xsd:anyURI                          |
| definition@ja | ORCID iD                            |
| definition@en | ORCID iD.                           |
| seeAlso       | https://orcid.org/                  |

| Property      | raid                               |
|---------------|------------------------------------|
| IRI           | https://purl.org/rdm/ontology/raid |
| subPropertyOf | rdm:identifierValue                |
| domain        | rdm:Project                        |
| range         | xsd:string                         |
| definition@ja | RAiD                               |
| definition@en | RAiD.                              |
| seeAlso       | https://raid.org/                  |

| Property      | ror                               |
|---------------|-----------------------------------|
| IRI           | https://purl.org/rdm/ontology/ror |
| subPropertyOf | rdm:identifierValue               |
| domain        | rdm:Institution                   |
| range         | xsd:anyURI                        |
| definition@ja | ROR ID                            |
| definition@en | ROR ID.                           |
| seeAlso       | https://ror.org/                  |

| Property      | isbn                               |
|---------------|------------------------------------|
| IRI           | https://purl.org/rdm/ontology/isbn |
| domain        | rdm:Book                           |
| range         | xsd:string                         |
| definition@en | ISBN code.                         |
| definition@ja | ISBNコード                            |

| Property      | japanGrantNumber                               |
|---------------|------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/japanGrantNumber |
| domain        | rdm:Grant                                      |
| range         | xsd:string                                     |
| definition@en | Japan grant number.                            |
| definition@ja | 体系的課題番号                                        |
| seeAlso       | https://www.nistep.go.jp/archives/53002        |

| Property      | keywords                                 |
|---------------|------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/keywords   |
| domain        | rdm:Resource                             |
| range         | xsd:string                               |
| definition@en | Keywords used to describe this Resource. |
| definition@ja | キーワード                                    |

| Property      | language                               |
|---------------|----------------------------------------|
| IRI           | https://purl.org/rdm/ontology/language |
| domain        | rdm:Resource                           |
| range         | xsd:language                           |
| definition@en | The language of this Resource.         |
| definition@ja | 言語                                     |

| Property      | localIdentifier                               |
|---------------|-----------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/localIdentifier |
| domain        | rdm:Experiment ,rdm:Resource                  |
| definition@en | Local identifier.                             |
| definition@ja | ローカル識別子                                       |

| Property      | location                                                                  |
|---------------|---------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/location                                    |
| domain        | rdm:Event ,rdm:Resource                                                   |
| range         | xsd:string                                                                |
| definition@en | The place where this Event was/will be held or this Resource was created. |
| definition@ja | 主語クラスの開催場所・取得場所                                                           |

| Property      | measurementTechnique                                            |
|---------------|-----------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/measurementTechnique              |
| domain        | rdm:DataManagementPlan                                          |
| range         | xsd:string                                                      |
| definition@en | A technique, method or technology used to create research data. |
| definition@ja | 研究データの収集・取得方法                                                   |

| Property      | name                                                                                                                             |
|---------------|----------------------------------------------------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/name                                                                                               |
| domain        | rdm:Event ,rdm:Grant ,rdm:Institution ,rdm:License ,rdm:Project ,rdm:Repository ,rdm:Resource ,rdm:Role ,rdm:SoftwareApplication |
| range         | xsd:string                                                                                                                       |
| definition@en | A name of this Class.                                                                                                            |
| definition@ja | 主語クラスの名称                                                                                                                         |

| Property      | additionalName                                       |
|---------------|------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/additionalName         |
| subPropertyOf | rdm:name                                             |
| domain        | rdm:Person                                           |
| definition@en | An additional name for this Person e.g. middle name. |
| definition@ja | ミドルネームなど、その他の名前                                      |

| Property      | familyName                               |
|---------------|------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/familyName |
| subPropertyOf | rdm:name                                 |
| domain        | rdm:Person                               |
| definition@en | Family name.                             |
| definition@ja | 名字                                       |

| Property      | givenName                               |
|---------------|-----------------------------------------|
| IRI           | https://purl.org/rdm/ontology/givenName |
| subPropertyOf | rdm:name                                |
| domain        | rdm:Person                              |
| definition@en | Given name.                             |
| definition@ja | ファーストネーム                                |

| Property      | identifierName                               |
|---------------|----------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/identifierName |
| subPropertyOf | rdm:name                                     |
| domain        | rdm:Identifier                               |
| definition@en | A name of identifier scheme e.g. DOI.        |
| definition@ja | 識別子のスキーマ名                                    |

| Property      | operatingSystem                                          |
|---------------|----------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/operatingSystem            |
| domain        | rdm:SoftwareApplication                                  |
| range         | xsd:string                                               |
| definition@en | Operating systems supported by this SoftwareApplication. |
| definition@ja | アプリケーションがサポートされているOS                                     |

| Property      | orcid                               |
|---------------|-------------------------------------|
| IRI           | https://purl.org/rdm/ontology/orcid |
| domain        | rdm:Person                          |
| range         | xsd:anyURI                          |
| definition@ja | ORCID iD                            |
| definition@en | ORCID iD.                           |
| seeAlso       | https://orcid.org/                  |

| Property      | processorRequirements                                            |
|---------------|------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/processorRequirements              |
| domain        | rdm:SoftwareApplication                                          |
| range         | xsd:string                                                       |
| definition@en | Processor architecture required to run this SoftwareApplication. |
| definition@ja | アプリケーション実行に必要なプロセッサー要件                                           |

| Property      | protocolText                               |
|---------------|--------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/protocolText |
| domain        | rdm:Experiment                             |
| definition@en | A text of protocol of this Experiment.     |
| definition@ja | 実験のプロトコル、手順を示したテキスト                        |

| Property      | purpose                                                                               |
|---------------|---------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/purpose                                                 |
| domain        | rdm:Event                                                                             |
| range         | xsd:string                                                                            |
| definition@en | Context of this Event implementation e.g. reasons and backgrounds for implementation. |
| definition@ja | 実施に至った理由や背景など、イベント実施のコンテクスト                                                           |

| Property      | query                                   |
|---------------|-----------------------------------------|
| IRI           | https://purl.org/rdm/ontology/query     |
| domain        | rdm:Search                              |
| range         | xsd:string                              |
| definition@ja | Search クラスで検索時に使われたクエリ                  |
| definition@en | The query used on this Search activity. |

| Property      | raid                               |
|---------------|------------------------------------|
| IRI           | https://purl.org/rdm/ontology/raid |
| domain        | rdm:Project                        |
| range         | xsd:string                         |
| definition@ja | RAiD                               |
| definition@en | RAiD.                              |
| seeAlso       | https://raid.org/                  |

| Property      | readme                                                     |
|---------------|------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/readme                       |
| domain        | rdm:SoftwareApplication                                    |
| definition@en | A text description as Read Me of this SoftwareApplication. |
| definition@ja | README                                                     |

| Property      | ror                               |
|---------------|-----------------------------------|
| IRI           | https://purl.org/rdm/ontology/ror |
| domain        | rdm:Institution                   |
| range         | xsd:anyURI                        |
| definition@ja | ROR ID                            |
| definition@en | ROR ID.                           |
| seeAlso       | https://ror.org/                  |

| Property      | sdDatePublished                               |
|---------------|-----------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/sdDatePublished |
| domain        | rdm:Resource                                  |
| definition@en | The acquisition date of this Resource.        |
| definition@ja | 外部ファイルの取得日                                    |

| Property      | sha256                               |
|---------------|--------------------------------------|
| IRI           | https://purl.org/rdm/ontology/sha256 |
| domain        | rdm:Resource                         |
| range         | xsd:string                           |
| definition@en | sha256 hash value.                   |
| definition@ja | sha256のハッシュ値                         |

| Property      | size                               |
|---------------|------------------------------------|
| IRI           | https://purl.org/rdm/ontology/size |
| domain        | rdm:Resource                       |
| range         | xsd:nonNegativeInteger ,xsd:string |
| definition@en | This Resource size.                |
| definition@ja | 主語クラスの大きさ、サイズ                      |

| Property      | approximateSize                                                               |
|---------------|-------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/approximateSize                                 |
| subPropertyOf | rdm:size                                                                      |
| domain        | rdm:DataManagementPlan                                                        |
| range         | xsd:string                                                                    |
| definition@en | Approximate size of research data to be described in this DataManagementPlan. |
| definition@ja | DMPにおける概略データ量                                                                 |

| Property      | collectionSize                               |
|---------------|----------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/collectionSize |
| subPropertyOf | rdm:size                                     |
| domain        | rdm:Collection                               |
| range         | xsd:nonNegativeInteger                       |
| definition@en | The number of items in this Collection.      |
| definition@ja | 所定のパッケージに含まれるデータセットの総数                       |

| Property      | softwareRequirements                                            |
|---------------|-----------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/softwareRequirements              |
| domain        | rdm:SoftwareApplication                                         |
| range         | xsd:string                                                      |
| definition@en | Component dependency requirements for this SoftwareApplication. |
| definition@ja | アプリケーションコンポーネントの依存要件                                            |

| Property      | specialRequirements                               |
|---------------|---------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/specialRequirements |
| domain        | rdm:SoftwareApplication                           |
| range         | xsd:string                                        |
| definition@en | Other requirements for this SoftwareApplication.  |
| definition@ja | 他のプロパティに当てはまらないアプリケーションに必要な条件                     |

| Property      | storageRequirements                               |
|---------------|---------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/storageRequirements |
| domain        | rdm:SoftwareApplication                           |
| range         | xsd:string                                        |
| definition@en | Storage requirements.                             |
| definition@ja | ストレージの要件                                          |

| Property      | textContent                               |
|---------------|-------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/textContent |
| domain        | rdm:Resource                              |
| range         | xsd:string                                |
| definition@ja | Resource の内容であるテキスト                       |
| definition@en | The textual content of this Resource.     |

| Property      | url                                                                               |
|---------------|-----------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/url                                                 |
| domain        | rdm:Grant ,rdm:Identifier ,rdm:License ,rdm:Project ,rdm:Repository ,rdm:Resource |
| range         | xsd:anyURI                                                                        |
| definition@en | A URL related to this Class.                                                      |
| definition@ja | 主語クラスに関連するURL                                                                     |

| Property      | value                                                        |
|---------------|--------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/value                          |
| range         | xsd:anyURI ,xsd:double ,xsd:integer ,xsd:string              |
| definition@en | A higer-level property that indicates some value of Classes. |
| definition@ja | クラスにおける何かしらの値を示す上位プロパティ                                      |

| Property      | hashValue                               |
|---------------|-----------------------------------------|
| IRI           | https://purl.org/rdm/ontology/hashValue |
| subPropertyOf | rdm:value                               |
| domain        | rdm:Resource                            |
| range         | xsd:string                              |
| definition@en | Hash value.                             |
| definition@ja | ハッシュ値                                   |

| Property      | sha256                               |
|---------------|--------------------------------------|
| IRI           | https://purl.org/rdm/ontology/sha256 |
| subPropertyOf | rdm:hashValue                        |
| domain        | rdm:Resource                         |
| range         | xsd:string                           |
| definition@en | sha256 hash value.                   |
| definition@ja | sha256のハッシュ値                         |

| Property      | identifierValue                               |
|---------------|-----------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/identifierValue |
| subPropertyOf | rdm:value                                     |
| domain        | rdm:Identifier                                |
| range         | xsd:anyURI ,xsd:string                        |
| definition@en | Identifier value.                             |
| definition@ja | 識別子の値                                         |

| Property      | doi                               |
|---------------|-----------------------------------|
| IRI           | https://purl.org/rdm/ontology/doi |
| subPropertyOf | rdm:identifierValue               |
| domain        | rdm:Project ,rdm:Resource         |
| range         | xsd:anyURI                        |
| definition@ja | DOI                               |
| definition@en | DOI URL.                          |
| seeAlso       | https://www.doi.org/              |

| Property      | eradResearcherNumber                               |
|---------------|----------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/eradResearcherNumber |
| subPropertyOf | rdm:identifierValue                                |
| domain        | rdm:Person                                         |
| range         | xsd:string                                         |
| definition@en | e-rad researcher number.                           |
| definition@ja | e-rad 研究者番号                                        |
| seeAlso       | https://www.e-rad.go.jp/                           |

| Property      | funderId                                           |
|---------------|----------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/funderId             |
| subPropertyOf | rdm:identifierValue                                |
| domain        | rdm:FundingAgency                                  |
| range         | xsd:string                                         |
| definition@en | Funder ID.                                         |
| definition@ja | 助成機関識別子                                            |
| seeAlso       | https://www.crossref.org/services/funder-registry/ |

| Property      | isbn                               |
|---------------|------------------------------------|
| IRI           | https://purl.org/rdm/ontology/isbn |
| subPropertyOf | rdm:identifierValue                |
| domain        | rdm:Book                           |
| range         | xsd:string                         |
| definition@en | ISBN code.                         |
| definition@ja | ISBNコード                            |

| Property      | japanGrantNumber                               |
|---------------|------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/japanGrantNumber |
| subPropertyOf | rdm:identifierValue                            |
| domain        | rdm:Grant                                      |
| range         | xsd:string                                     |
| definition@en | Japan grant number.                            |
| definition@ja | 体系的課題番号                                        |
| seeAlso       | https://www.nistep.go.jp/archives/53002        |

| Property      | localIdentifier                               |
|---------------|-----------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/localIdentifier |
| subPropertyOf | rdm:identifierValue                           |
| domain        | rdm:Experiment ,rdm:Resource                  |
| definition@en | Local identifier.                             |
| definition@ja | ローカル識別子                                       |

| Property      | orcid                               |
|---------------|-------------------------------------|
| IRI           | https://purl.org/rdm/ontology/orcid |
| subPropertyOf | rdm:identifierValue                 |
| domain        | rdm:Person                          |
| range         | xsd:anyURI                          |
| definition@ja | ORCID iD                            |
| definition@en | ORCID iD.                           |
| seeAlso       | https://orcid.org/                  |

| Property      | raid                               |
|---------------|------------------------------------|
| IRI           | https://purl.org/rdm/ontology/raid |
| subPropertyOf | rdm:identifierValue                |
| domain        | rdm:Project                        |
| range         | xsd:string                         |
| definition@ja | RAiD                               |
| definition@en | RAiD.                              |
| seeAlso       | https://raid.org/                  |

| Property      | ror                               |
|---------------|-----------------------------------|
| IRI           | https://purl.org/rdm/ontology/ror |
| subPropertyOf | rdm:identifierValue               |
| domain        | rdm:Institution                   |
| range         | xsd:anyURI                        |
| definition@ja | ROR ID                            |
| definition@en | ROR ID.                           |
| seeAlso       | https://ror.org/                  |

| Property      | version                               |
|---------------|---------------------------------------|
| IRI           | https://purl.org/rdm/ontology/version |
| domain        | rdm:Resource ,rdm:SoftwareApplication |
| range         | xsd:nonNegativeInteger ,xsd:string    |
| definition@en | The version of this Class.            |
| definition@ja | バージョン                                 |

### Object Property

| Property      | accessRightsInformation                               |
|---------------|-------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/accessRightsInformation |
| domain        | rdm:Project ,rdm:Resource                             |
| range         | rdm:AccessRights                                      |
| definition@en | Information on access rights of this Class.           |
| definition@ja | クラスのアクセス権関連情報                                         |

| Property      | dataAccessRightsInformation                                              |
|---------------|--------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/dataAccessRightsInformation                |
| subPropertyOf | rdm:accessRightsInformation                                              |
| domain        | rdm:DataManagementPlan                                                   |
| definition@ja | DMPにおけるデータへのアクセス権                                                        |
| definition@en | Information on access rights to be described in this DataManagementPlan. |

| Property      | activityObject                                                                                                          |
|---------------|-------------------------------------------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/activityObject                                                                            |
| domain        | rdm:Activity                                                                                                            |
| range         | rdm:Collection ,rdm:Event ,rdm:Experiment ,rdm:Project ,rdm:Repository ,rdm:Resource ,rdm:Role ,rdm:SoftwareApplication |
| definition@en | An object of the Activity.                                                                                              |
| definition@ja | 行動の対象物                                                                                                                  |

| Property      | affiliation                                          |
|---------------|------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/affiliation            |
| domain        | rdm:Person                                           |
| range         | rdm:Institution                                      |
| definition@en | An organization that this Person is affiliated with. |
| definition@ja | 人物の所属先機関                                             |

| Property      | agent                                            |
|---------------|--------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/agent              |
| domain        | rdm:Activity                                     |
| range         | rdm:Institution ,rdm:Person                      |
| definition@en | The direct performer or driver of this Activity. |
| definition@ja | 行動・行為の直接的な実施者                                    |

| Property      | cites                                                                                            |
|---------------|--------------------------------------------------------------------------------------------------|
| inverseOf     | rdm:isCitedBy                                                                                    |
| domain        | rdm:Resource                                                                                     |
| range         | rdm:Resource                                                                                     |
| definition@en | A Resource that this Class cites.                                                                |
| definition@ja | 主語クラスが引用しているリソース                                                                                 |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#cites |

| Property      | collectedIn                                                          |
|---------------|----------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/collectedIn                            |
| inverseOf     | rdm:collectionItem                                                   |
| domain        | rdm:Resource                                                         |
| range         | rdm:Collection                                                       |
| definition@en | A Collection which includes this Resource as a member of Collection. |
| definition@ja | リソースをメンバーとして含むCollection                                             |

| Property      | collectionItem                          |
|---------------|-----------------------------------------|
| domain        | rdm:Collection                          |
| range         | rdm:Resource                            |
| definition@en | A Resource included in this Collection. |
| definition@ja | コレクションに含まれるリソース                         |

| Property      | collects                                                                                            |
|---------------|-----------------------------------------------------------------------------------------------------|
| inverseOf     | rdm:isCollectedBy                                                                                   |
| domain        | rdm:Collection ,rdm:Resource ,rdm:SoftwareApplication                                               |
| range         | rdm:Collection ,rdm:Resource ,rdm:SoftwareApplication                                               |
| definition@en | A Class which collected/created by using this Class.                                                |
| definition@ja | 主語クラスを使用して収集・作成されたクラス                                                                               |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#collects |

| Property      | compiles                                                                                            |
|---------------|-----------------------------------------------------------------------------------------------------|
| inverseOf     | rdm:isCompiledBy                                                                                    |
| domain        | rdm:Resource ,rdm:SoftwareApplication                                                               |
| range         | rdm:Resource ,rdm:SoftwareApplication                                                               |
| definition@en | The result of a compile or creation event using this Class.                                         |
| definition@ja | 主語クラスを使用したコンパイルまたは作成イベントの結果                                                                         |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#compiles |

| Property      | conditionOfAccess                               |
|---------------|-------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/conditionOfAccess |
| domain        | rdm:AccessRights                                |
| range         | rdm:RightsStatement                             |
| definition@en | Access rights type.                             |
| definition@ja | アクセス権の種別                                        |

| Property      | continues                                                                                            |
|---------------|------------------------------------------------------------------------------------------------------|
| inverseOf     | rdm:isContinuedBy                                                                                    |
| domain        | rdm:Event ,rdm:Institution ,rdm:Project ,rdm:Repository ,rdm:Resource ,rdm:SoftwareApplication       |
| range         | rdm:Event ,rdm:Institution ,rdm:Project ,rdm:Repository ,rdm:Resource ,rdm:SoftwareApplication       |
| definition@en | A Class of which this Class is a continuation.                                                       |
| definition@ja | 主語クラスが継続しているクラス                                                                                      |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#continues |

| Property      | contributor                                                                                   |
|---------------|-----------------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/contributor                                                     |
| domain        | rdm:Collection ,rdm:Event ,rdm:Experiment ,rdm:Project ,rdm:Resource ,rdm:SoftwareApplication |
| range         | rdm:Institution ,rdm:Person                                                                   |
| definition@en | A contributor to this Class.                                                                  |
| definition@ja | クラスへの寄与者                                                                                      |

| Property      | creator                               |
|---------------|---------------------------------------|
| IRI           | https://purl.org/rdm/ontology/creator |
| subPropertyOf | rdm:contributor                       |
| domain        | rdm:Resource ,rdm:SoftwareApplication |
| range         | rdm:Person                            |
| definition@en | The creator/author of this Resource.  |
| definition@ja | リソースの作成者                              |

| Property      | dataCreator                                                              |
|---------------|--------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/dataCreator                                |
| subPropertyOf | rdm:creator                                                              |
| domain        | rdm:DataManagementPlan                                                   |
| range         | rdm:Person                                                               |
| definition@ja | DMPにおける研究データの作成者                                                         |
| definition@en | The creator of research data to be described in this DataManagementPlan. |

| Property      | dataManager                                                                   |
|---------------|-------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/dataManager                                     |
| subPropertyOf | rdm:contributor                                                               |
| domain        | rdm:DataManagementPlan                                                        |
| range         | rdm:Person                                                                    |
| definition@ja | DMPにおける研究データ管理者                                                               |
| definition@en | The data manager of research data to be described in this DataManagementPlan. |

| Property      | experimenter                                                 |
|---------------|--------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/experimenter                   |
| subPropertyOf | rdm:contributor                                              |
| domain        | rdm:Experiment                                               |
| range         | rdm:Person                                                   |
| definition@en | The practitioner, performer and executor of this Experiment. |
| definition@ja | 実験の実施者、実行者                                                   |

| Property      | hostingInstitution                                                                                             |
|---------------|----------------------------------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/hostingInstitution                                                               |
| subPropertyOf | rdm:contributor                                                                                                |
| domain        | rdm:DataManagementPlan ,rdm:Project ,rdm:Resource                                                              |
| range         | rdm:Institution                                                                                                |
| definition@ja | (Project に属する)Resource の管理機関、もしくはDMPにおける研究データ管理機関                                                              |
| definition@en | The hosting institution of Resource (in Project) and research data to be described in this DataManagementPlan. |

| Property      | identifierManager                                                          |
|---------------|----------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/identifierManager                            |
| subPropertyOf | rdm:contributor                                                            |
| domain        | rdm:Identifier                                                             |
| range         | rdm:Institution                                                            |
| definition@en | A manager of identifier scheme/service, e.g. International DOI Foundation. |
| definition@ja | 国際DOI財団など、識別子の管理者                                                          |

| Property      | organizer                               |
|---------------|-----------------------------------------|
| IRI           | https://purl.org/rdm/ontology/organizer |
| subPropertyOf | rdm:contributor                         |
| domain        | rdm:Event                               |
| definition@en | An Event organizer or host.             |
| definition@ja | イベントの開催者、主催者                            |

| Property      | researcher                               |
|---------------|------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/researcher |
| subPropertyOf | rdm:contributor                          |
| domain        | rdm:Project                              |
| range         | rdm:Person                               |
| definition@en | A researcher involved in this Project.   |
| definition@ja | プロジェクトに参加した研究者                           |

| Property      | creator                               |
|---------------|---------------------------------------|
| domain        | rdm:Resource ,rdm:SoftwareApplication |
| range         | rdm:Person                            |
| definition@en | The creator/author of this Resource.  |
| definition@ja | リソースの作成者                              |

| Property      | dataCreator                                                              |
|---------------|--------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/dataCreator                                |
| subPropertyOf | rdm:creator                                                              |
| domain        | rdm:DataManagementPlan                                                   |
| range         | rdm:Person                                                               |
| definition@ja | DMPにおける研究データの作成者                                                         |
| definition@en | The creator of research data to be described in this DataManagementPlan. |

| Property      | dataAccessRightsInformation                                              |
|---------------|--------------------------------------------------------------------------|
| domain        | rdm:DataManagementPlan                                                   |
| definition@ja | DMPにおけるデータへのアクセス権                                                        |
| definition@en | Information on access rights to be described in this DataManagementPlan. |

| Property      | dataCreator                                                              |
|---------------|--------------------------------------------------------------------------|
| domain        | rdm:DataManagementPlan                                                   |
| range         | rdm:Person                                                               |
| definition@ja | DMPにおける研究データの作成者                                                         |
| definition@en | The creator of research data to be described in this DataManagementPlan. |

| Property      | dataIdentifier                                                              |
|---------------|-----------------------------------------------------------------------------|
| domain        | rdm:DataManagementPlan                                                      |
| range         | rdm:Identifier                                                              |
| definition@ja | DMPにおけるデータ識別子                                                               |
| definition@en | The identifier of research data to be described in this DataManagementPlan. |

| Property      | dataLicenseInformation                                                   |
|---------------|--------------------------------------------------------------------------|
| domain        | rdm:DataManagementPlan                                                   |
| definition@ja | DMPにおけるデータのライセンス                                                         |
| definition@en | The license of research data to be described in this DataManagementPlan. |

| Property      | dataManager                                                                   |
|---------------|-------------------------------------------------------------------------------|
| domain        | rdm:DataManagementPlan                                                        |
| range         | rdm:Person                                                                    |
| definition@ja | DMPにおける研究データ管理者                                                               |
| definition@en | The data manager of research data to be described in this DataManagementPlan. |

| Property      | describes                                                                                            |
|---------------|------------------------------------------------------------------------------------------------------|
| inverseOf     | rdm:isDescribedBy                                                                                    |
| domain        | rdm:Resource                                                                                         |
| definition@en | A Class that this Resource describes.                                                                |
| definition@ja | Resource が説明しているクラス                                                                                  |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#continues |

| Property      | dmp                                                        |
|---------------|------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/dmp                          |
| domain        | rdm:Project ,rdm:Resource                                  |
| range         | rdm:DataManagementPlan                                     |
| definition@en | Contents of data management plan of this Project/Resource. |
| definition@ja | 資源やプロジェクトに紐づくデータ管理計画                                       |

| Property      | dmpFormatProvider                                            |
|---------------|--------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/dmpFormatProvider              |
| domain        | rdm:DataManagementPlan                                       |
| range         | rdm:Institution                                              |
| definition@en | A institution which provides this DataManagementPlan format. |
| definition@ja | DMP種別の提供者                                                    |

| Property      | dmpTargetItem                               |
|---------------|---------------------------------------------|
| domain        | rdm:DataManagementPlan                      |
| range         | rdm:Resource                                |
| definition@en | A Resource described in DataManagementPlan. |
| definition@ja | DMPで対象になっているリソース                            |

| Property      | documents                                                                                            |
|---------------|------------------------------------------------------------------------------------------------------|
| inverseOf     | rdm:isDocumentedBy                                                                                   |
| domain        | rdm:Resource                                                                                         |
| range         | rdm:SoftwareApplication                                                                              |
| definition@en | A  SoftwareApplication which is documented by this Resource.                                         |
| definition@ja | Resource がその説明文書・ドキュメントに相当する SoftwareApplication                                                     |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#documents |

| Property      | experimenter                                                 |
|---------------|--------------------------------------------------------------|
| domain        | rdm:Experiment                                               |
| range         | rdm:Person                                                   |
| definition@en | The practitioner, performer and executor of this Experiment. |
| definition@ja | 実験の実施者、実行者                                                   |

| Property      | fromLocation                            |
|---------------|-----------------------------------------|
| domain        | rdm:Download ,rdm:Upload                |
| range         | rdm:Repository ,rdm:SoftwareApplication |
| definition@en | Uploaded or downloaded from             |
| definition@ja | アップロードもしくはダウンロード元                       |

| Property      | funder                                                                                  |
|---------------|-----------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/funder                                                    |
| domain        | rdm:Grant ,rdm:Project ,rdm:Resource                                                    |
| range         | rdm:FundingAgency                                                                       |
| definition@en | An organization that funds this Project or research activities to create this Resource. |
| definition@ja | 研究資金プログラム提供者                                                                            |

| Property      | funding                                                                          |
|---------------|----------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/funding                                            |
| domain        | rdm:Project ,rdm:Resource                                                        |
| range         | rdm:Grant                                                                        |
| definition@en | A grant program for this Project or research activities to create this Resource. |
| definition@ja | 研究資金プログラム                                                                        |

| Property      | hasMetadata                                                                                          |
|---------------|------------------------------------------------------------------------------------------------------|
| inverseOf     | rdm:isMetadataFor                                                                                    |
| domain        | rdm:Collection ,rdm:Project ,rdm:Resource                                                            |
| range         | rdm:MetadataDocument                                                                                 |
| definition@en | A Resource which has additional metadata of this Class.                                              |
| definition@ja | 主語クラスの追加メタデータを持つ Resource                                                                            |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#continues |

| Property      | hasPart                                                                                                        |
|---------------|----------------------------------------------------------------------------------------------------------------|
| inverseOf     | rdm:isPartOf                                                                                                   |
| domain        | rdm:Collection ,rdm:Experiment ,rdm:Grant ,rdm:Institution ,rdm:Project ,rdm:Resource ,rdm:SoftwareApplication |
| definition@en | A class consisting of multiple parts of which this class is a part.                                            |
| definition@ja | 主語クラスが一部分となっている、複数の部分から成るクラス                                                                                   |

| Property      | hasVersion                                                                                               |
|---------------|----------------------------------------------------------------------------------------------------------|
| inverseOf     | rdm:isVersionOf                                                                                          |
| domain        | rdm:Collection ,rdm:Resource ,rdm:SoftwareApplication                                                    |
| range         | rdm:Collection ,rdm:Resource ,rdm:SoftwareApplication                                                    |
| definition@en | A Class  which is another version of this Class.                                                         |
| definition@ja | 主語クラスの異なるバージョンとして存在するクラス                                                                                 |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#ismetadatafor |

| Property      | hostingInstitution                                                                                             |
|---------------|----------------------------------------------------------------------------------------------------------------|
| domain        | rdm:DataManagementPlan ,rdm:Project ,rdm:Resource                                                              |
| range         | rdm:Institution                                                                                                |
| definition@ja | (Project に属する)Resource の管理機関、もしくはDMPにおける研究データ管理機関                                                              |
| definition@en | The hosting institution of Resource (in Project) and research data to be described in this DataManagementPlan. |

| Property      | identifierInformation                                                                             |
|---------------|---------------------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/identifierInformation                                               |
| domain        | rdm:Collection ,rdm:Grant ,rdm:Institution ,rdm:Person ,rdm:Project ,rdm:Repository ,rdm:Resource |
| range         | rdm:Identifier                                                                                    |
| definition@en | An identifier information of this Class.                                                          |
| definition@ja | 識別子                                                                                               |

| Property      | dataIdentifier                                                              |
|---------------|-----------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/dataIdentifier                                |
| subPropertyOf | rdm:identifierInformation                                                   |
| domain        | rdm:DataManagementPlan                                                      |
| range         | rdm:Identifier                                                              |
| definition@ja | DMPにおけるデータ識別子                                                               |
| definition@en | The identifier of research data to be described in this DataManagementPlan. |

| Property      | identifierManager                                                          |
|---------------|----------------------------------------------------------------------------|
| domain        | rdm:Identifier                                                             |
| range         | rdm:Institution                                                            |
| definition@en | A manager of identifier scheme/service, e.g. International DOI Foundation. |
| definition@ja | 国際DOI財団など、識別子の管理者                                                          |

| Property      | inProject                                      |
|---------------|------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/inProject        |
| inverseOf     | rdm:projectItem                                |
| domain        | rdm:Resource                                   |
| range         | rdm:Project                                    |
| definition@en | A Project this Resource is within/included in. |
| definition@ja | リソースが属するプロジェクト                                 |

| Property      | inclusionRelation                                                              |
|---------------|--------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/inclusionRelation                                |
| definition@en | A higher-level property that indicates inclusion relationship between Classes. |
| definition@ja | 主語クラスと包含関係のあるクラスを指す上位プロパティ                                                     |

| Property      | hasPart                                                                                                        |
|---------------|----------------------------------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/hasPart                                                                          |
| subPropertyOf | rdm:inclusionRelation                                                                                          |
| inverseOf     | rdm:isPartOf                                                                                                   |
| domain        | rdm:Collection ,rdm:Experiment ,rdm:Grant ,rdm:Institution ,rdm:Project ,rdm:Resource ,rdm:SoftwareApplication |
| definition@en | A class consisting of multiple parts of which this class is a part.                                            |
| definition@ja | 主語クラスが一部分となっている、複数の部分から成るクラス                                                                                   |

| Property      | isPartOf                                                                                                       |
|---------------|----------------------------------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/isPartOf                                                                         |
| subPropertyOf | rdm:inclusionRelation                                                                                          |
| domain        | rdm:Collection ,rdm:Experiment ,rdm:Grant ,rdm:Institution ,rdm:Project ,rdm:Resource ,rdm:SoftwareApplication |
| definition@en | A Class of the parts that make up this class                                                                   |
| definition@ja | 主語クラスを構成する部分のクラス                                                                                               |

| Property      | instrument                                                                        |
|---------------|-----------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/instrument                                          |
| domain        | rdm:Activity ,rdm:Experiment                                                      |
| definition@en | The object that helped the agent perform the Activity and used in the Experiment. |
| definition@ja | 行動や実験で使われた道具、ツール                                                                  |

| Property      | isCitedBy                                                                                            |
|---------------|------------------------------------------------------------------------------------------------------|
| domain        | rdm:Resource                                                                                         |
| range         | rdm:Resource                                                                                         |
| definition@en | A Resource that this Class is cited.                                                                 |
| definition@ja | 主語クラスが引用されているリソース                                                                                    |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#iscitedby |

| Property      | isCollectedBy                                                                                            |
|---------------|----------------------------------------------------------------------------------------------------------|
| domain        | rdm:Collection ,rdm:Resource ,rdm:SoftwareApplication                                                    |
| range         | rdm:Collection ,rdm:Resource ,rdm:SoftwareApplication                                                    |
| definition@en | A Class that is used to collect/create this Class.                                                       |
| definition@ja | 主語クラスの収集・生成に利用されたクラス                                                                                     |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#iscollectedby |

| Property      | isCompiledBy                                                                                            |
|---------------|---------------------------------------------------------------------------------------------------------|
| domain        | rdm:Resource ,rdm:SoftwareApplication                                                                   |
| range         | rdm:Resource ,rdm:SoftwareApplication                                                                   |
| definition@en | A Class used to compile or create this Class.                                                           |
| definition@ja | 主語クラスをコンパイルまたは作成するために使用するクラス                                                                            |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#iscompiledby |

| Property      | isContinuedBy                                                                                            |
|---------------|----------------------------------------------------------------------------------------------------------|
| domain        | rdm:Event ,rdm:Institution ,rdm:Project ,rdm:Repository ,rdm:Resource ,rdm:SoftwareApplication           |
| range         | rdm:Event ,rdm:Institution ,rdm:Project ,rdm:Repository ,rdm:Resource ,rdm:SoftwareApplication           |
| definition@en | A Class continued by this Class                                                                          |
| definition@ja | 主語クラスが継続されているクラス                                                                                         |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#iscontinuedby |

| Property      | isDerivedFrom                                                                                            |
|---------------|----------------------------------------------------------------------------------------------------------|
| inverseOf     | rdm:isSourceOf                                                                                           |
| domain        | rdm:Collection ,rdm:Project ,rdm:Resource                                                                |
| range         | rdm:Collection ,rdm:Project ,rdm:Resource                                                                |
| definition@en | A Class on which this Class is based.                                                                    |
| definition@ja | 主語クラスが基づいているクラス                                                                                          |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#isderivedfrom |

| Property      | isDescribedBy                                                                                        |
|---------------|------------------------------------------------------------------------------------------------------|
| range         | rdm:Resource                                                                                         |
| definition@en | A Resource that describes this Class.                                                                |
| definition@ja | 主語クラスを説明している Resource                                                                                |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#continues |

| Property      | isDocumentedBy                                                                                            |
|---------------|-----------------------------------------------------------------------------------------------------------|
| domain        | rdm:SoftwareApplication                                                                                   |
| range         | rdm:Resource                                                                                              |
| definition@en | A Resource which is documentation about/explaining this SoftwareApplication.                              |
| definition@ja | SoftwareApplication の説明文書・ドキュメントである Resource                                                              |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#isdocumentedby |

| Property      | isIdenticalTo                                                                                            |
|---------------|----------------------------------------------------------------------------------------------------------|
| domain        | rdm:Resource                                                                                             |
| definition@en | A Resource which is identical to this Resource.                                                          |
| definition@ja | 主語クラスと同一である Resource                                                                                     |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#isidenticalto |

| Property      | isMetadataFor                                                                                            |
|---------------|----------------------------------------------------------------------------------------------------------|
| domain        | rdm:MetadataDocument                                                                                     |
| range         | rdm:Collection ,rdm:Project ,rdm:Resource                                                                |
| definition@en | A Class for which this Resource has additional metadata.                                                 |
| definition@ja | Resource が追加メタデータになっているクラス                                                                               |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#ismetadatafor |

| Property      | isNewVersionOf                                                                                            |
|---------------|-----------------------------------------------------------------------------------------------------------|
| inverseOf     | rdm:isPreviousVersionOf                                                                                   |
| domain        | rdm:Collection ,rdm:Resource ,rdm:SoftwareApplication                                                     |
| range         | rdm:Collection ,rdm:Resource ,rdm:SoftwareApplication                                                     |
| definition@en | A Class which is a new edition of this Class.                                                             |
| definition@ja | 主語クラスが新版に当たる、旧版のクラス                                                                                       |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#isnewversionof |

| Property      | isObsoletedBy                                                                                            |
|---------------|----------------------------------------------------------------------------------------------------------|
| inverseOf     | rdm:obsoletes                                                                                            |
| definition@en | A Class which replaces this Class.                                                                       |
| definition@ja | 主語クラスを廃止させたクラス                                                                                           |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#isobsoletedby |

| Property      | isOriginalFormOf                                                                                            |
|---------------|-------------------------------------------------------------------------------------------------------------|
| inverseOf     | rdm:isVariantFormOf                                                                                         |
| domain        | rdm:Resource ,rdm:SoftwareApplication                                                                       |
| range         | rdm:Resource ,rdm:SoftwareApplication                                                                       |
| definition@en | A Class of which this Class is the original form.                                                           |
| definition@ja | 主語クラスをオリジナルとするクラス                                                                                           |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#isoriginalformof |

| Property      | isPartOf                                                                                                       |
|---------------|----------------------------------------------------------------------------------------------------------------|
| domain        | rdm:Collection ,rdm:Experiment ,rdm:Grant ,rdm:Institution ,rdm:Project ,rdm:Resource ,rdm:SoftwareApplication |
| definition@en | A Class of the parts that make up this class                                                                   |
| definition@ja | 主語クラスを構成する部分のクラス                                                                                               |

| Property      | isPreviousVersionOf                                                                                            |
|---------------|----------------------------------------------------------------------------------------------------------------|
| domain        | rdm:Collection ,rdm:Resource ,rdm:SoftwareApplication                                                          |
| range         | rdm:Collection ,rdm:Resource ,rdm:SoftwareApplication                                                          |
| definition@en | A Class which is a previous edition of this Class.                                                             |
| definition@ja | 主語クラスが旧版に当たる、新版のクラス                                                                                            |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#ispreviousversionof |

| Property      | isPublishedIn                                                                                                  |
|---------------|----------------------------------------------------------------------------------------------------------------|
| domain        | rdm:Collection ,rdm:Project ,rdm:Resource ,rdm:SoftwareApplication                                             |
| range         | rdm:Collection ,rdm:Project ,rdm:Resource ,rdm:SoftwareApplication                                             |
| definition@en | A Class which is published in this Class.                                                                      |
| definition@ja | 主語クラスをその一部として公開するクラス                                                                                           |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#ispreviousversionof |

| Property      | isReferencedBy                                                                                            |
|---------------|-----------------------------------------------------------------------------------------------------------|
| inverseOf     | rdm:references                                                                                            |
| domain        | rdm:Collection ,rdm:Project ,rdm:Resource ,rdm:SoftwareApplication                                        |
| range         | rdm:Collection ,rdm:Project ,rdm:Resource ,rdm:SoftwareApplication                                        |
| definition@en | A Class which uses this Class as a source of information.                                                 |
| definition@ja | 主語クラスを情報源として参照しているクラス                                                                                     |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#isreferencedby |

| Property      | isRelatedTo                                                      |
|---------------|------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/isRelatedTo                        |
| definition@en | A Class independent of this Class that is related to this Class. |
| definition@ja | 主語クラスと何らかの関連がある、独立したクラス                                          |

| Property      | cites                                                                                            |
|---------------|--------------------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/cites                                                              |
| subPropertyOf | rdm:isRelatedTo                                                                                  |
| inverseOf     | rdm:isCitedBy                                                                                    |
| domain        | rdm:Resource                                                                                     |
| range         | rdm:Resource                                                                                     |
| definition@en | A Resource that this Class cites.                                                                |
| definition@ja | 主語クラスが引用しているリソース                                                                                 |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#cites |

| Property      | collects                                                                                            |
|---------------|-----------------------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/collects                                                              |
| subPropertyOf | rdm:isRelatedTo                                                                                     |
| inverseOf     | rdm:isCollectedBy                                                                                   |
| domain        | rdm:Collection ,rdm:Resource ,rdm:SoftwareApplication                                               |
| range         | rdm:Collection ,rdm:Resource ,rdm:SoftwareApplication                                               |
| definition@en | A Class which collected/created by using this Class.                                                |
| definition@ja | 主語クラスを使用して収集・作成されたクラス                                                                               |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#collects |

| Property      | compiles                                                                                            |
|---------------|-----------------------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/compiles                                                              |
| subPropertyOf | rdm:isRelatedTo                                                                                     |
| inverseOf     | rdm:isCompiledBy                                                                                    |
| domain        | rdm:Resource ,rdm:SoftwareApplication                                                               |
| range         | rdm:Resource ,rdm:SoftwareApplication                                                               |
| definition@en | The result of a compile or creation event using this Class.                                         |
| definition@ja | 主語クラスを使用したコンパイルまたは作成イベントの結果                                                                         |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#compiles |

| Property      | continues                                                                                            |
|---------------|------------------------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/continues                                                              |
| subPropertyOf | rdm:isRelatedTo                                                                                      |
| inverseOf     | rdm:isContinuedBy                                                                                    |
| domain        | rdm:Event ,rdm:Institution ,rdm:Project ,rdm:Repository ,rdm:Resource ,rdm:SoftwareApplication       |
| range         | rdm:Event ,rdm:Institution ,rdm:Project ,rdm:Repository ,rdm:Resource ,rdm:SoftwareApplication       |
| definition@en | A Class of which this Class is a continuation.                                                       |
| definition@ja | 主語クラスが継続しているクラス                                                                                      |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#continues |

| Property      | describes                                                                                            |
|---------------|------------------------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/describes                                                              |
| subPropertyOf | rdm:isRelatedTo                                                                                      |
| inverseOf     | rdm:isDescribedBy                                                                                    |
| domain        | rdm:Resource                                                                                         |
| definition@en | A Class that this Resource describes.                                                                |
| definition@ja | Resource が説明しているクラス                                                                                  |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#continues |

| Property      | documents                                                                                            |
|---------------|------------------------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/documents                                                              |
| subPropertyOf | rdm:isRelatedTo                                                                                      |
| inverseOf     | rdm:isDocumentedBy                                                                                   |
| domain        | rdm:Resource                                                                                         |
| range         | rdm:SoftwareApplication                                                                              |
| definition@en | A  SoftwareApplication which is documented by this Resource.                                         |
| definition@ja | Resource がその説明文書・ドキュメントに相当する SoftwareApplication                                                     |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#documents |

| Property      | hasMetadata                                                                                          |
|---------------|------------------------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/hasMetadata                                                            |
| subPropertyOf | rdm:isRelatedTo                                                                                      |
| inverseOf     | rdm:isMetadataFor                                                                                    |
| domain        | rdm:Collection ,rdm:Project ,rdm:Resource                                                            |
| range         | rdm:MetadataDocument                                                                                 |
| definition@en | A Resource which has additional metadata of this Class.                                              |
| definition@ja | 主語クラスの追加メタデータを持つ Resource                                                                            |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#continues |

| Property      | hasVersion                                                                                               |
|---------------|----------------------------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/hasVersion                                                                 |
| subPropertyOf | rdm:isRelatedTo                                                                                          |
| inverseOf     | rdm:isVersionOf                                                                                          |
| domain        | rdm:Collection ,rdm:Resource ,rdm:SoftwareApplication                                                    |
| range         | rdm:Collection ,rdm:Resource ,rdm:SoftwareApplication                                                    |
| definition@en | A Class  which is another version of this Class.                                                         |
| definition@ja | 主語クラスの異なるバージョンとして存在するクラス                                                                                 |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#ismetadatafor |

| Property      | isCitedBy                                                                                            |
|---------------|------------------------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/isCitedBy                                                              |
| subPropertyOf | rdm:isRelatedTo                                                                                      |
| domain        | rdm:Resource                                                                                         |
| range         | rdm:Resource                                                                                         |
| definition@en | A Resource that this Class is cited.                                                                 |
| definition@ja | 主語クラスが引用されているリソース                                                                                    |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#iscitedby |

| Property      | isCollectedBy                                                                                            |
|---------------|----------------------------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/isCollectedBy                                                              |
| subPropertyOf | rdm:isRelatedTo                                                                                          |
| domain        | rdm:Collection ,rdm:Resource ,rdm:SoftwareApplication                                                    |
| range         | rdm:Collection ,rdm:Resource ,rdm:SoftwareApplication                                                    |
| definition@en | A Class that is used to collect/create this Class.                                                       |
| definition@ja | 主語クラスの収集・生成に利用されたクラス                                                                                     |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#iscollectedby |

| Property      | isCompiledBy                                                                                            |
|---------------|---------------------------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/isCompiledBy                                                              |
| subPropertyOf | rdm:isRelatedTo                                                                                         |
| domain        | rdm:Resource ,rdm:SoftwareApplication                                                                   |
| range         | rdm:Resource ,rdm:SoftwareApplication                                                                   |
| definition@en | A Class used to compile or create this Class.                                                           |
| definition@ja | 主語クラスをコンパイルまたは作成するために使用するクラス                                                                            |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#iscompiledby |

| Property      | isContinuedBy                                                                                            |
|---------------|----------------------------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/isContinuedBy                                                              |
| subPropertyOf | rdm:isRelatedTo                                                                                          |
| domain        | rdm:Event ,rdm:Institution ,rdm:Project ,rdm:Repository ,rdm:Resource ,rdm:SoftwareApplication           |
| range         | rdm:Event ,rdm:Institution ,rdm:Project ,rdm:Repository ,rdm:Resource ,rdm:SoftwareApplication           |
| definition@en | A Class continued by this Class                                                                          |
| definition@ja | 主語クラスが継続されているクラス                                                                                         |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#iscontinuedby |

| Property      | isDerivedFrom                                                                                            |
|---------------|----------------------------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/isDerivedFrom                                                              |
| subPropertyOf | rdm:isRelatedTo                                                                                          |
| inverseOf     | rdm:isSourceOf                                                                                           |
| domain        | rdm:Collection ,rdm:Project ,rdm:Resource                                                                |
| range         | rdm:Collection ,rdm:Project ,rdm:Resource                                                                |
| definition@en | A Class on which this Class is based.                                                                    |
| definition@ja | 主語クラスが基づいているクラス                                                                                          |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#isderivedfrom |

| Property      | isDescribedBy                                                                                        |
|---------------|------------------------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/isDescribedBy                                                          |
| subPropertyOf | rdm:isRelatedTo                                                                                      |
| range         | rdm:Resource                                                                                         |
| definition@en | A Resource that describes this Class.                                                                |
| definition@ja | 主語クラスを説明している Resource                                                                                |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#continues |

| Property      | isDocumentedBy                                                                                            |
|---------------|-----------------------------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/isDocumentedBy                                                              |
| subPropertyOf | rdm:isRelatedTo                                                                                           |
| domain        | rdm:SoftwareApplication                                                                                   |
| range         | rdm:Resource                                                                                              |
| definition@en | A Resource which is documentation about/explaining this SoftwareApplication.                              |
| definition@ja | SoftwareApplication の説明文書・ドキュメントである Resource                                                              |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#isdocumentedby |

| Property      | isIdenticalTo                                                                                            |
|---------------|----------------------------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/isIdenticalTo                                                              |
| subPropertyOf | rdm:isRelatedTo                                                                                          |
| domain        | rdm:Resource                                                                                             |
| definition@en | A Resource which is identical to this Resource.                                                          |
| definition@ja | 主語クラスと同一である Resource                                                                                     |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#isidenticalto |

| Property      | isMetadataFor                                                                                            |
|---------------|----------------------------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/isMetadataFor                                                              |
| subPropertyOf | rdm:isRelatedTo                                                                                          |
| domain        | rdm:MetadataDocument                                                                                     |
| range         | rdm:Collection ,rdm:Project ,rdm:Resource                                                                |
| definition@en | A Class for which this Resource has additional metadata.                                                 |
| definition@ja | Resource が追加メタデータになっているクラス                                                                               |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#ismetadatafor |

| Property      | isNewVersionOf                                                                                            |
|---------------|-----------------------------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/isNewVersionOf                                                              |
| subPropertyOf | rdm:isRelatedTo                                                                                           |
| inverseOf     | rdm:isPreviousVersionOf                                                                                   |
| domain        | rdm:Collection ,rdm:Resource ,rdm:SoftwareApplication                                                     |
| range         | rdm:Collection ,rdm:Resource ,rdm:SoftwareApplication                                                     |
| definition@en | A Class which is a new edition of this Class.                                                             |
| definition@ja | 主語クラスが新版に当たる、旧版のクラス                                                                                       |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#isnewversionof |

| Property      | isObsoletedBy                                                                                            |
|---------------|----------------------------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/isObsoletedBy                                                              |
| subPropertyOf | rdm:isRelatedTo                                                                                          |
| inverseOf     | rdm:obsoletes                                                                                            |
| definition@en | A Class which replaces this Class.                                                                       |
| definition@ja | 主語クラスを廃止させたクラス                                                                                           |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#isobsoletedby |

| Property      | isOriginalFormOf                                                                                            |
|---------------|-------------------------------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/isOriginalFormOf                                                              |
| subPropertyOf | rdm:isRelatedTo                                                                                             |
| inverseOf     | rdm:isVariantFormOf                                                                                         |
| domain        | rdm:Resource ,rdm:SoftwareApplication                                                                       |
| range         | rdm:Resource ,rdm:SoftwareApplication                                                                       |
| definition@en | A Class of which this Class is the original form.                                                           |
| definition@ja | 主語クラスをオリジナルとするクラス                                                                                           |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#isoriginalformof |

| Property      | isPreviousVersionOf                                                                                            |
|---------------|----------------------------------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/isPreviousVersionOf                                                              |
| subPropertyOf | rdm:isRelatedTo                                                                                                |
| domain        | rdm:Collection ,rdm:Resource ,rdm:SoftwareApplication                                                          |
| range         | rdm:Collection ,rdm:Resource ,rdm:SoftwareApplication                                                          |
| definition@en | A Class which is a previous edition of this Class.                                                             |
| definition@ja | 主語クラスが旧版に当たる、新版のクラス                                                                                            |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#ispreviousversionof |

| Property      | isPublishedIn                                                                                                  |
|---------------|----------------------------------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/isPublishedIn                                                                    |
| subPropertyOf | rdm:isRelatedTo                                                                                                |
| domain        | rdm:Collection ,rdm:Project ,rdm:Resource ,rdm:SoftwareApplication                                             |
| range         | rdm:Collection ,rdm:Project ,rdm:Resource ,rdm:SoftwareApplication                                             |
| definition@en | A Class which is published in this Class.                                                                      |
| definition@ja | 主語クラスをその一部として公開するクラス                                                                                           |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#ispreviousversionof |

| Property      | isReferencedBy                                                                                            |
|---------------|-----------------------------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/isReferencedBy                                                              |
| subPropertyOf | rdm:isRelatedTo                                                                                           |
| inverseOf     | rdm:references                                                                                            |
| domain        | rdm:Collection ,rdm:Project ,rdm:Resource ,rdm:SoftwareApplication                                        |
| range         | rdm:Collection ,rdm:Project ,rdm:Resource ,rdm:SoftwareApplication                                        |
| definition@en | A Class which uses this Class as a source of information.                                                 |
| definition@ja | 主語クラスを情報源として参照しているクラス                                                                                     |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#isreferencedby |

| Property      | isRequiredBy                                                                                            |
|---------------|---------------------------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/isRequiredBy                                                              |
| subPropertyOf | rdm:isRelatedTo                                                                                         |
| inverseOf     | rdm:requires                                                                                            |
| domain        | rdm:Resource ,rdm:SoftwareApplication                                                                   |
| range         | rdm:Resource ,rdm:SoftwareApplication                                                                   |
| definition@en | A Class which requires this Class.                                                                      |
| definition@ja | 主語クラスを必要とするクラス                                                                                          |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#isrequiredby |

| Property      | isReviewedBy                                                                                            |
|---------------|---------------------------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/isReviewedBy                                                              |
| subPropertyOf | rdm:isRelatedTo                                                                                         |
| inverseOf     | rdm:reviews                                                                                             |
| domain        | rdm:Resource ,rdm:SoftwareApplication                                                                   |
| range         | rdm:Review                                                                                              |
| definition@en | A Class which is a review of this Class.                                                                |
| definition@ja | 主語クラスのレビューとなっているクラス                                                                                     |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#isreviewedby |

| Property      | isSourceOf                                                                                            |
|---------------|-------------------------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/isSourceOf                                                              |
| subPropertyOf | rdm:isRelatedTo                                                                                       |
| domain        | rdm:Collection ,rdm:Project ,rdm:Resource                                                             |
| range         | rdm:Collection ,rdm:Project ,rdm:Resource                                                             |
| definition@en | A Class from which this Class is derived.                                                             |
| definition@ja | 主語クラスが基となっているクラス                                                                                      |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#issourceof |

| Property      | isSupplementTo                                                                                            |
|---------------|-----------------------------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/isSupplementTo                                                              |
| subPropertyOf | rdm:isRelatedTo                                                                                           |
| inverseOf     | rdm:isSupplementedBy                                                                                      |
| domain        | rdm:Collection ,rdm:Project ,rdm:Resource                                                                 |
| range         | rdm:Collection ,rdm:Project ,rdm:Resource                                                                 |
| definition@en | A Class that supplements this Class.                                                                      |
| definition@ja | 主語クラスが補足をしているクラス                                                                                          |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#issupplementto |

| Property      | isSupplementedBy                                                                                          |
|---------------|-----------------------------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/isSupplementedBy                                                            |
| subPropertyOf | rdm:isRelatedTo                                                                                           |
| domain        | rdm:Collection ,rdm:Project ,rdm:Resource                                                                 |
| range         | rdm:Collection ,rdm:Project ,rdm:Resource                                                                 |
| definition@en | A Class which is supplemented by this Class.                                                              |
| definition@ja | 主語クラスを補足しているクラス                                                                                           |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#issupplementby |

| Property      | isVariantFormOf                                                                                            |
|---------------|------------------------------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/isVariantFormOf                                                              |
| subPropertyOf | rdm:isRelatedTo                                                                                            |
| domain        | rdm:Resource ,rdm:SoftwareApplication                                                                      |
| range         | rdm:Resource ,rdm:SoftwareApplication                                                                      |
| definition@en | A Class which is the original form of this Class.                                                          |
| definition@ja | 主語クラスのオリジナルであるクラス                                                                                          |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#isvariantformof |

| Property      | isVersionOf                                                                                            |
|---------------|--------------------------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/isVersionOf                                                              |
| subPropertyOf | rdm:isRelatedTo                                                                                        |
| domain        | rdm:Collection ,rdm:Resource ,rdm:SoftwareApplication                                                  |
| range         | rdm:Collection ,rdm:Resource ,rdm:SoftwareApplication                                                  |
| definition@en | A Class  which this Class has as an another version.                                                   |
| definition@ja | 主語クラスが異なるバージョンであるクラス                                                                                   |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#isversionof |

| Property      | obsoletes                                                                                            |
|---------------|------------------------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/obsoletes                                                              |
| subPropertyOf | rdm:isRelatedTo                                                                                      |
| definition@en | A Class which is replaced by this Class.                                                             |
| definition@ja | 主語クラスによって置き換えられたクラス                                                                                  |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#obsoletes |

| Property      | references                                                                                            |
|---------------|-------------------------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/references                                                              |
| subPropertyOf | rdm:isRelatedTo                                                                                       |
| domain        | rdm:Collection ,rdm:Project ,rdm:Resource ,rdm:SoftwareApplication                                    |
| range         | rdm:Collection ,rdm:Project ,rdm:Resource ,rdm:SoftwareApplication                                    |
| definition@en | A Class which is used as a source of information by this Class.                                       |
| definition@ja | 主語クラスの情報源となったクラス                                                                                      |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#references |

| Property      | requires                                                                                            |
|---------------|-----------------------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/requires                                                              |
| subPropertyOf | rdm:isRelatedTo                                                                                     |
| domain        | rdm:Resource ,rdm:SoftwareApplication                                                               |
| range         | rdm:Resource ,rdm:SoftwareApplication                                                               |
| definition@en | A Class which is required by this Class.                                                            |
| definition@ja | 主語クラスを必要とするクラス                                                                                      |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#requires |

| Property      | reviews                                                                                            |
|---------------|----------------------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/reviews                                                              |
| subPropertyOf | rdm:isRelatedTo                                                                                    |
| domain        | rdm:Review                                                                                         |
| range         | rdm:Resource ,rdm:SoftwareApplication                                                              |
| definition@en | A Class which is reviewed by this Class.                                                           |
| definition@ja | 主語クラスによってレビューされたクラス                                                                                |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#reviews |

| Property      | isRequiredBy                                                                                            |
|---------------|---------------------------------------------------------------------------------------------------------|
| inverseOf     | rdm:requires                                                                                            |
| domain        | rdm:Resource ,rdm:SoftwareApplication                                                                   |
| range         | rdm:Resource ,rdm:SoftwareApplication                                                                   |
| definition@en | A Class which requires this Class.                                                                      |
| definition@ja | 主語クラスを必要とするクラス                                                                                          |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#isrequiredby |

| Property      | isReviewedBy                                                                                            |
|---------------|---------------------------------------------------------------------------------------------------------|
| inverseOf     | rdm:reviews                                                                                             |
| domain        | rdm:Resource ,rdm:SoftwareApplication                                                                   |
| range         | rdm:Review                                                                                              |
| definition@en | A Class which is a review of this Class.                                                                |
| definition@ja | 主語クラスのレビューとなっているクラス                                                                                     |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#isreviewedby |

| Property      | isSourceOf                                                                                            |
|---------------|-------------------------------------------------------------------------------------------------------|
| domain        | rdm:Collection ,rdm:Project ,rdm:Resource                                                             |
| range         | rdm:Collection ,rdm:Project ,rdm:Resource                                                             |
| definition@en | A Class from which this Class is derived.                                                             |
| definition@ja | 主語クラスが基となっているクラス                                                                                      |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#issourceof |

| Property      | isSupplementTo                                                                                            |
|---------------|-----------------------------------------------------------------------------------------------------------|
| inverseOf     | rdm:isSupplementedBy                                                                                      |
| domain        | rdm:Collection ,rdm:Project ,rdm:Resource                                                                 |
| range         | rdm:Collection ,rdm:Project ,rdm:Resource                                                                 |
| definition@en | A Class that supplements this Class.                                                                      |
| definition@ja | 主語クラスが補足をしているクラス                                                                                          |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#issupplementto |

| Property      | isSupplementedBy                                                                                          |
|---------------|-----------------------------------------------------------------------------------------------------------|
| domain        | rdm:Collection ,rdm:Project ,rdm:Resource                                                                 |
| range         | rdm:Collection ,rdm:Project ,rdm:Resource                                                                 |
| definition@en | A Class which is supplemented by this Class.                                                              |
| definition@ja | 主語クラスを補足しているクラス                                                                                           |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#issupplementby |

| Property      | isVariantFormOf                                                                                            |
|---------------|------------------------------------------------------------------------------------------------------------|
| domain        | rdm:Resource ,rdm:SoftwareApplication                                                                      |
| range         | rdm:Resource ,rdm:SoftwareApplication                                                                      |
| definition@en | A Class which is the original form of this Class.                                                          |
| definition@ja | 主語クラスのオリジナルであるクラス                                                                                          |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#isvariantformof |

| Property      | isVersionOf                                                                                            |
|---------------|--------------------------------------------------------------------------------------------------------|
| domain        | rdm:Collection ,rdm:Resource ,rdm:SoftwareApplication                                                  |
| range         | rdm:Collection ,rdm:Resource ,rdm:SoftwareApplication                                                  |
| definition@en | A Class  which this Class has as an another version.                                                   |
| definition@ja | 主語クラスが異なるバージョンであるクラス                                                                                   |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#isversionof |

| Property      | item                               |
|---------------|------------------------------------|
| IRI           | https://purl.org/rdm/ontology/item |
| range         | rdm:Resource                       |
| definition@en | A Resource related to this Class.  |
| definition@ja | 主語クラスと関連のあるリソース                    |

| Property      | collectionItem                               |
|---------------|----------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/collectionItem |
| subPropertyOf | rdm:item                                     |
| domain        | rdm:Collection                               |
| range         | rdm:Resource                                 |
| definition@en | A Resource included in this Collection.      |
| definition@ja | コレクションに含まれるリソース                              |

| Property      | dmpTargetItem                               |
|---------------|---------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/dmpTargetItem |
| subPropertyOf | rdm:item                                    |
| domain        | rdm:DataManagementPlan                      |
| range         | rdm:Resource                                |
| definition@en | A Resource described in DataManagementPlan. |
| definition@ja | DMPで対象になっているリソース                            |

| Property      | projectItem                               |
|---------------|-------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/projectItem |
| subPropertyOf | rdm:item                                  |
| domain        | rdm:Project                               |
| range         | rdm:Resource                              |
| definition@en | A Resource within this Project.           |
| definition@ja | プロジェクトに含まれるリソース                           |

| Property      | storedItem                               |
|---------------|------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/storedItem |
| subPropertyOf | rdm:item                                 |
| domain        | rdm:Repository                           |
| range         | rdm:Resource                             |
| definition@en | A Resource stored in this Repository.    |
| definition@ja | リポジトリに保存されている資源                          |

| Property      | licenseInformation                               |
|---------------|--------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/licenseInformation |
| domain        | rdm:Project ,rdm:Resource                        |
| range         | rdm:License                                      |
| definition@en | Information on license of this Class.            |
| definition@ja | プロジェクトやリソースのライセンス情報                              |

| Property      | dataLicenseInformation                                                   |
|---------------|--------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/dataLicenseInformation                     |
| subPropertyOf | rdm:licenseInformation                                                   |
| domain        | rdm:DataManagementPlan                                                   |
| definition@ja | DMPにおけるデータのライセンス                                                         |
| definition@en | The license of research data to be described in this DataManagementPlan. |

| Property      | material                                |
|---------------|-----------------------------------------|
| IRI           | https://purl.org/rdm/ontology/material  |
| domain        | rdm:Experiment                          |
| definition@en | Materials and inputs in the Experiment. |
| definition@ja | 実験における、材料や入力となるもの                       |

| Property      | obsoletes                                                                                            |
|---------------|------------------------------------------------------------------------------------------------------|
| definition@en | A Class which is replaced by this Class.                                                             |
| definition@ja | 主語クラスによって置き換えられたクラス                                                                                  |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#obsoletes |

| Property      | organizer                   |
|---------------|-----------------------------|
| domain        | rdm:Event                   |
| definition@en | An Event organizer or host. |
| definition@ja | イベントの開催者、主催者                |

| Property      | projectItem                     |
|---------------|---------------------------------|
| domain        | rdm:Project                     |
| range         | rdm:Resource                    |
| definition@en | A Resource within this Project. |
| definition@ja | プロジェクトに含まれるリソース                 |

| Property      | protocol                               |
|---------------|----------------------------------------|
| IRI           | https://purl.org/rdm/ontology/protocol |
| domain        | rdm:Experiment                         |
| definition@en | The protocol of this Experiment.       |
| definition@ja | 実験のプロトコル、手順                            |

| Property      | recipient                                                               |
|---------------|-------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/recipient                                 |
| domain        | rdm:Activity                                                            |
| range         | rdm:Person                                                              |
| definition@en | The recipient of this Activity and the affected party of this Activity. |
| definition@ja | 行動を受け取る・行動の影響を受ける相手                                                     |

| Property      | references                                                                                            |
|---------------|-------------------------------------------------------------------------------------------------------|
| domain        | rdm:Collection ,rdm:Project ,rdm:Resource ,rdm:SoftwareApplication                                    |
| range         | rdm:Collection ,rdm:Project ,rdm:Resource ,rdm:SoftwareApplication                                    |
| definition@en | A Class which is used as a source of information by this Class.                                       |
| definition@ja | 主語クラスの情報源となったクラス                                                                                      |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#references |

| Property      | requires                                                                                            |
|---------------|-----------------------------------------------------------------------------------------------------|
| domain        | rdm:Resource ,rdm:SoftwareApplication                                                               |
| range         | rdm:Resource ,rdm:SoftwareApplication                                                               |
| definition@en | A Class which is required by this Class.                                                            |
| definition@ja | 主語クラスを必要とするクラス                                                                                      |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#requires |

| Property      | researcher                             |
|---------------|----------------------------------------|
| domain        | rdm:Project                            |
| range         | rdm:Person                             |
| definition@en | A researcher involved in this Project. |
| definition@ja | プロジェクトに参加した研究者                         |

| Property      | result                                            |
|---------------|---------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/result              |
| inverseOf     | rdm:wasGeneratedBy                                |
| domain        | rdm:Activity ,rdm:Experiment                      |
| range         | rdm:Collection ,rdm:Project ,rdm:Resource         |
| definition@en | The result produced in this Activity /Experiment. |
| definition@ja | アクションや実験によって生成された新しいエンティティ                        |

| Property      | reviews                                                                                            |
|---------------|----------------------------------------------------------------------------------------------------|
| domain        | rdm:Review                                                                                         |
| range         | rdm:Resource ,rdm:SoftwareApplication                                                              |
| definition@en | A Class which is reviewed by this Class.                                                           |
| definition@ja | 主語クラスによってレビューされたクラス                                                                                |
| seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#reviews |

| Property      | storedIn                                              |
|---------------|-------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/storedIn                |
| inverseOf     | rdm:storedItem                                        |
| domain        | rdm:Resource                                          |
| range         | rdm:Repository                                        |
| definition@en | Repository or storage where this Resource is managed. |
| definition@ja | リソースが管理されているリポジトリやストレージ                               |

| Property      | storedItem                            |
|---------------|---------------------------------------|
| domain        | rdm:Repository                        |
| range         | rdm:Resource                          |
| definition@en | A Resource stored in this Repository. |
| definition@ja | リポジトリに保存されている資源                       |

| Property      | target                                                                             |
|---------------|------------------------------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/target                                               |
| domain        | rdm:Activity                                                                       |
| range         | rdm:Collection ,rdm:Project ,rdm:Repository ,rdm:Resource ,rdm:SoftwareApplication |
| definition@en | The indirect object, or target, of this Activity.                                  |
| definition@ja | アクションの間接的な対象物                                                                      |

| Property      | fromLocation                               |
|---------------|--------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/fromLocation |
| subPropertyOf | rdm:target                                 |
| domain        | rdm:Download ,rdm:Upload                   |
| range         | rdm:Repository ,rdm:SoftwareApplication    |
| definition@en | Uploaded or downloaded from                |
| definition@ja | アップロードもしくはダウンロード元                          |

| Property      | toLocation                                           |
|---------------|------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/toLocation             |
| subPropertyOf | rdm:target                                           |
| domain        | rdm:Download ,rdm:Preserve ,rdm:Register ,rdm:Upload |
| range         | rdm:Repository ,rdm:SoftwareApplication              |
| definition@en | Upload or Download location                          |
| definition@ja | アップロードもしくはダウンロード先の場所                                 |

| Property      | thumbnail                               |
|---------------|-----------------------------------------|
| IRI           | https://purl.org/rdm/ontology/thumbnail |
| domain        | rdm:Resource                            |
| range         | rdm:Image                               |
| definition@en | A thumbnail of this Resource.           |
| definition@ja | サムネイル                                   |

| Property      | toLocation                                           |
|---------------|------------------------------------------------------|
| domain        | rdm:Download ,rdm:Preserve ,rdm:Register ,rdm:Upload |
| range         | rdm:Repository ,rdm:SoftwareApplication              |
| definition@en | Upload or Download location                          |
| definition@ja | アップロードもしくはダウンロード先の場所                                 |

| Property      | wasGeneratedBy                                             |
|---------------|------------------------------------------------------------|
| IRI           | https://purl.org/rdm/ontology/wasGeneratedBy               |
| domain        | rdm:Collection ,rdm:Project ,rdm:Resource                  |
| range         | rdm:Activity ,rdm:Experiment                               |
| definition@en | Activity or Experiment which created/generated this Class. |
| definition@ja | 主語クラスが生成されたアクションまたは実験                                      |

## Named Individual

| Named Individual   | EmbargoedAccess                                                                           |
|--------------------|-------------------------------------------------------------------------------------------|
| IRI                | https://purl.org/rdm/ontology/EmbargoedAccess                                             |
| type               | rdm:RightsStatement                                                                       |
| definition@en      | Embargoed access (metadata only access until released for open access on a certain date). |
| definition@ja      | 公開期間猶予                                                                                    |
| sameAs             | http://purl.org/coar/access_right/c_f1cf                                                  |

| Named Individual   | MetadataOnlyAccess                               |
|--------------------|--------------------------------------------------|
| IRI                | https://purl.org/rdm/ontology/MetadataOnlyAccess |
| type               | rdm:RightsStatement                              |
| definition@en      | Metadata only access.                            |
| definition@ja      | メタデータのみ公開                                        |
| sameAs             | http://purl.org/coar/access_right/c_14cb         |

| Named Individual   | OpenAccess                               |
|--------------------|------------------------------------------|
| IRI                | https://purl.org/rdm/ontology/OpenAccess |
| type               | rdm:RightsStatement                      |
| definition@en      | Open access.                             |
| definition@ja      | 公開                                       |
| sameAs             | http://purl.org/coar/access_right/c_abf2 |

| Named Individual   | RestrictedAccess                               |
|--------------------|------------------------------------------------|
| IRI                | https://purl.org/rdm/ontology/RestrictedAccess |
| type               | rdm:RightsStatement                            |
| definition@en      | Restricted access.                             |
| definition@ja      | 限定公開                                           |
| sameAs             | http://purl.org/coar/access_right/c_16ec       |
