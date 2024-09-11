# Usage Guidelines

There is two domain models of RDM Ontology; focused on Resource and focused on Activity. The former is focused on describing Resource as a outcome of research activities. The latter is focused on research activities itself. These two can be linked by using rdm property, however, it is not recommended because of the complexity.

## Domain Model Focused on Resource

![Resource domain model](domain_model_Resource.png)

To describe research outcomes such as research data, the main entity should be of type Resource. (It is recommended that a subclass of Resource be selected and used according to the category of research outcomes.) Related entities such as research project can be described by linking to the main entity. Activity entities is not recommended to add to this style of describing to divide the result of research activity (Resource) and the process (Activity).
Examples of Resource focused description is in two formats:

- [JSON-LD](../example/example_research_data.json)
- [turtle](../example/example_research_data.ttl)

## Domain Model Focused on Activity

![Resource domain model](domain_model_Activity.png)

To describe research activities as a log, the main entity should be a subclass of Activity class. Resource entities can be linked as a result, a target and a used tool of the activity. Linking other entities to Resource is not recommended when the main entity is subclass of Activity, as well as Resourced focused case.

# Term Definitions Overview

| prefix | Namespace                                   |
| ------ | ------------------------------------------- |
| rdm    | https://purl.org/rdm/ontology/              |
| owl    | http://www.w3.org/2002/07/owl#              |
| rdf    | http://www.w3.org/1999/02/22-rdf-syntax-ns# |
| rdfs   | http://www.w3.org/2000/01/rdf-schema#       |
| xsd    | http://www.w3.org/2001/XMLSchema#           |

The following is a legend of term description.
||Term|
|--|--|
|URI|URI to the term|
|rdfs:comment|Comment in English<br>Comment in Japanese|
|rdf:type|owl:ObjectProperty or owl:DatatypeProperty|
|rdfs:subClassOf/rdfs:subPropertyOf|Super class/property|
|owl:inverseOf| Inverse property|
|rdfs:domain|Domain class. Any of classes in list can be domain when multiple classes are listed. (unionOf)|
|rdfs:range|Range class or datatype. Any of these in list can be range when multiple items are listed.(unionOf)|
|note|Additional description|
|activityObject / agent / recipient / result / target| Classes that can be used as the value of rdm:activityClass /rdm:agent / rdm:recipient / rdm:result / rdm:target property in a subclass of an Activity entity. |

## Classes

|              | rdm:Activity                           |
| ------------ | -------------------------------------- |
| URI          | https://purl.org/rdm/ontology/Activity |
| rdfs:comment | An action or activity.<br>行動や行為   |

|                 | rdm:Accept                                                                |
| --------------- | ------------------------------------------------------------------------- |
| URI             | https://purl.org/rdm/ontology/Accept                                      |
| rdfs:comment    | An act of approving Resource or request.<br>Resource や依頼を承認する行動 |
| rdfs:subClassOf | rdm:Activity                                                              |
| activityObject  | rdm:Resource                                                              |
| example         | データ管理者が、データキュレーションが行われたデータセットを承認する      |

|                 | rdm:Align                                                                              |
| --------------- | -------------------------------------------------------------------------------------- |
| URI             | https://purl.org/rdm/ontology/Align                                                    |
| rdfs:comment    | An act of editing Resource to format.<br>Resource をフォーマットに合わせて編集する行動 |
| rdfs:subClassOf | rdm:Activity                                                                           |
| activityObject  | rdm:Resource                                                                           |
| agent           | rdm:Person                                                                             |
| result          | rdm:Resource                                                                           |
| example         | キュレーターが、提出されたデータを規定のフォーマットに合わせて編集する                 |

|                 | rdm:Anonymize                                                     |
| --------------- | ----------------------------------------------------------------- |
| URI             | https://purl.org/rdm/ontology/Anonymize                           |
| rdfs:comment    | An act of making Resource anonymous.<br>Resource を匿名化する行動 |
| rdfs:subClassOf | rdm:Activity                                                      |
| activityObject  | rdm:Resource                                                      |
| result          | rdm:Resource                                                      |
| example         | キュレーターが、個人情報が含まれたデータを匿名化処理する          |

|                 | rdm:Ask                                                                                                        |
| --------------- | -------------------------------------------------------------------------------------------------------------- |
| URI             | https://purl.org/rdm/ontology/Ask                                                                              |
| rdfs:comment    | An act of asking questions to Person, chatbot etc.<br>Person やチャットボットなどに質問をする行動              |
| rdfs:subClassOf | rdm:Activity                                                                                                   |
| activityObject  | rdm:Message                                                                                                    |
| recipient       | rdm:Person                                                                                                     |
| example         | データキュレーターが、キュレーション業務の依頼者に、不明瞭な点を質問する<br>研究者が、チャットボットに質問する |

|                 | rdm:Assign                                                                                                      |
| --------------- | --------------------------------------------------------------------------------------------------------------- |
| URI             | https://purl.org/rdm/ontology/Assign                                                                            |
| rdfs:comment    | An act of assigning a role to Person.<br>Person に役割を任命する行動                                            |
| rdfs:subClassOf | rdm:Activity                                                                                                    |
| activityObject  | rdm:Role                                                                                                        |
| recipient       | rdm:Person                                                                                                      |
| example         | PI が、データ管理者を任命する<br>データコーディネーターが、キュレーション依頼に対して、キュレーターを割り当てる |

|                 | rdm:Authorize                                                                                            |
| --------------- | -------------------------------------------------------------------------------------------------------- |
| URI             | https://purl.org/rdm/ontology/Authorize                                                                  |
| rdfs:comment    | An act of granting permission or right to an object.<br>権利や許可を与える行動                           |
| rdfs:subClassOf | rdm:Activity                                                                                             |
| activityObject  | rdm:RightsStatement                                                                                      |
| example         | 研究者が、新たにプロジェクトへの参加が決まった別の研究者に、プロジェクト内データへのアクセス権を付与する |

|                 | rdm:Check                                                                                                                                     |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| URI             | https://purl.org/rdm/ontology/Check                                                                                                           |
| rdfs:comment    | An act of checking the regulation for Resource, such as using checkboxes.<br>チェックボックスに印をつけるなど、規定の項目に関して確認する行動 |
| rdfs:subClassOf | rdm:Activity                                                                                                                                  |
| activityObject  | rdm:Resource                                                                                                                                  |
|                 |
| example         | キュレーターが、提出されたデータリストを確認する                                                                                              |

|                 | rdm:Cleanse                                                                               |
| --------------- | ----------------------------------------------------------------------------------------- |
| URI             | https://purl.org/rdm/ontology/Cleanse                                                     |
| rdfs:comment    | An act of performing data cleansing of Resource.<br>Resource をデータクレンジングする行動 |
| rdfs:subClassOf | rdm:Activity                                                                              |
| activityObject  | rdm:Resource                                                                              |
| agent           | rdm:Person                                                                                |
| result          | rdm:Resource                                                                              |
| example         | キュレーターが、提出されたデータをクレンジングする                                        |

|                 | rdm:Collect                                               |
| --------------- | --------------------------------------------------------- |
| URI             | https://purl.org/rdm/ontology/Collect                     |
| rdfs:comment    | An act of collecting Resource.<br>Resource を収集する行動 |
| rdfs:subClassOf | rdm:Activity                                              |
| activityObject  | rdm:Collection, rdm:Resource                              |
| result          | rdm:Collection, rdm:Resource                              |
| example         | 国会図書館が、ある大学のリポジトリから博士論文を収集する  |

|                 | rdm:Comment                                                                           |
| --------------- | ------------------------------------------------------------------------------------- |
| URI             | https://purl.org/rdm/ontology/Comment                                                 |
| rdfs:comment    | An act of generating a comment on Resource.<br>Resource に対してコメントをする行動    |
| rdfs:subClassOf | rdm:Activity                                                                          |
| activityObject  | rdm:Message                                                                           |
| target          | rdm:Resource                                                                          |
| example         | GRDM のコメント機能を利用して、研究者が GRDM に格納されている資料に対しコメントをする |

|                 | rdm:Connect                                                                              |
| --------------- | ---------------------------------------------------------------------------------------- |
| URI             | https://purl.org/rdm/ontology/Connect                                                    |
| rdfs:comment    | An act of connecting service to another service.<br>サービスを別のサービスに接続する行動 |
| rdfs:subClassOf | rdm:Activity                                                                             |
| activityObject  | rdm:Repository, rdm:SoftwareApplication                                                  |
| agent           | rdm:Person                                                                               |
| target          | rdm:Repository, rdm:SoftwareApplication                                                  |
| example         | 研究者が、アドオンを利用して GRDM に S3 を接続する                                       |

|                 | rdm:Convert                                                                                     |
| --------------- | ----------------------------------------------------------------------------------------------- |
| URI             | https://purl.org/rdm/ontology/Convert                                                           |
| rdfs:comment    | An act of converting Resource into a new Resource.<br>Resource を新たな Resource に変換する行動 |
| rdfs:subClassOf | rdm:Activity                                                                                    |
| activityObject  | rdm:Resource                                                                                    |
| result          | rdm:Resource                                                                                    |
| example         | キュレーターが、QuickTime files のデータを MPEG4 形式に変換する                                 |

|                 | rdm:Create                                                                                                                     |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| URI             | https://purl.org/rdm/ontology/Create                                                                                           |
| rdfs:comment    | An act of creating/producing/generating Resource, Project, Collection etc.<br>Project, Resource, Collection などを作成する行動 |
| rdfs:subClassOf | rdm:Activity                                                                                                                   |
| result          | rdm:Collection, rdm:DataManagementPlan, rdm:Project, rdm:Resource                                                              |
| example         | PI が、 ある研究プロジェクトに関する DMP を作成する                                                                            |

|                 | rdm:Dump                                                                            |
| --------------- | ----------------------------------------------------------------------------------- |
| URI             | https://purl.org/rdm/ontology/Dump                                                  |
| rdfs:comment    | An act of creating a log file by dumping.<br>ダンプによりログファイルを作成する行動 |
| rdfs:subClassOf | rdm:Create                                                                          |
| agent           | rdm:Person                                                                          |
| result          | rdm:Resource                                                                        |
| example         | 研究者が、研究で実施したデータ解析過程のログを書き出す                              |

|                 | rdm:Deploy                                                                                               |
| --------------- | -------------------------------------------------------------------------------------------------------- |
| URI             | https://purl.org/rdm/ontology/Deploy                                                                     |
| rdfs:comment    | An act of deploying SoftwareApplication or Resource.<br>Resource, SoftwareApplication をデプロイする行動 |
| rdfs:subClassOf | rdm:Activity                                                                                             |
| activityObject  | rdm:Resource, rdm:SoftwareApplication                                                                    |
| agent           | rdm:Person                                                                                               |
| example         | 研究者が、研究で利用するプログラムを計算機上に配置する                                                   |

|                 | rdm:Develop                                                     |
| --------------- | --------------------------------------------------------------- |
| URI             | https://purl.org/rdm/ontology/Develop                           |
| rdfs:comment    | An act of developing a program.<br>プログラミングで実装する行動 |
| rdfs:subClassOf | rdm:Activity                                                    |
| activityObject  | rdm:Resource, rdm:SoftwareApplication                           |
| agent           | rdm:Person                                                      |
| example         | 研究者が、研究で利用するプログラムを実装する                    |

|                 | rdm:Download                                                         |
| --------------- | -------------------------------------------------------------------- |
| URI             | https://purl.org/rdm/ontology/Download                               |
| rdfs:comment    | An act of downloading Resource.<br>Resource をダウンロードする行動   |
| rdfs:subClassOf | rdm:Activity                                                         |
| activityObject  | rdm:Resource                                                         |
| agent           | rdm:Person                                                           |
| example         | 研究者が、リポジトリにある研究データをローカル PC にダウンロードする |

|                 | rdm:Evaluate                                                                                     |
| --------------- | ------------------------------------------------------------------------------------------------ |
| URI             | https://purl.org/rdm/ontology/Evaluate                                                           |
| rdfs:comment    | An act of evaluating Resource, such as peer-review.<br>ピアレビューなど、Resource を評価する行動 |
| rdfs:subClassOf | rdm:Activity                                                                                     |
| activityObject  | rdm:Resource                                                                                     |
| agent           | rdm:Person                                                                                       |
| result          | rdm:Review                                                                                       |
| example         | データコーディネーターが、メタデータを評価する                                                   |

|                 | rdm:Execute                                                                                                                |
| --------------- | -------------------------------------------------------------------------------------------------------------------------- |
| URI             | https://purl.org/rdm/ontology/Execute                                                                                      |
| rdfs:comment    | An act of executing SoftwareApplication, Resource, program etc.<br>Resource, SoftwareApplication, プログラムを実行する行動 |
| rdfs:subClassOf | rdm:Activity                                                                                                               |
| activityObject  | rdm:Experiment, rdm:Resource                                                                                               |
| agent           | rdm:Person                                                                                                                 |
| result          | rdm:Resource                                                                                                               |
| example         | 研究者が、解析プログラムを実行しデータ解析を行う                                                                           |

|                 | rdm:Get                                                                                         |
| --------------- | ----------------------------------------------------------------------------------------------- |
| URI             | https://purl.org/rdm/ontology/Get                                                               |
| rdfs:comment    | An act of getting/obtaining Resource, information etc.<br>Resource または情報などを取得する行動 |
| rdfs:subClassOf | rdm:Activity                                                                                    |
| activityObject  | rdm:Resource                                                                                    |
| example         | DMP 担当者が、研究データのリストを取得する                                                      |

|                 | rdm:Inform                                                                                         |
| --------------- | -------------------------------------------------------------------------------------------------- |
| URI             | https://purl.org/rdm/ontology/Inform                                                               |
| rdfs:comment    | An act of notifying Person/Institution of information.<br>Person, Institution に対して通知する行動 |
| rdfs:subClassOf | rdm:Activity                                                                                       |
| activityObject  | rdm:Message                                                                                        |
| example         | データコーディネイターが、キュレーション依頼が完了したことを依頼者へ通知する                       |

|                 | rdm:Ingest                                                                                                                                                                           |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| URI             | https://purl.org/rdm/ontology/Ingest                                                                                                                                                 |
| rdfs:comment    | An act of getting and adding metadata to Resource from public information as part of data curation.<br>キュレーションの一環として、Resource のメタデータを外部から取得し付与する行動 |
| rdfs:subClassOf | rdm:Activity                                                                                                                                                                         |
| activityObject  | rdm:MetadataDocument                                                                                                                                                                 |
| agent           | rdm:Person                                                                                                                                                                           |
| result          | rdm:MetadataDocument                                                                                                                                                                 |
| example         | キュレーターが、提出されたデータに関連するメタデータを外部から取り込んで付与する                                                                                                     |

|                 | rdm:Integrate                                                                                                                       |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| URI             | https://purl.org/rdm/ontology/Integrate                                                                                             |
| rdfs:comment    | An act of integrating different forms of metadata as part of data curation.<br>キュレーションの一環として、メタデータを統合する行動 |
| rdfs:subClassOf | rdm:Activity                                                                                                                        |
| activityObject  | rdm:MetadataDocument                                                                                                                |
| agent           | rdm:Person                                                                                                                          |
| result          | rdm:MetadataDocument                                                                                                                |
| target          | rdm:MetadataDocument                                                                                                                |
| example         | データ管理者が、ある Resource に対する複数のメタデータを一つに統合する                                                              |

|                 | rdm:Preserve                                                                                                                                          |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| URI             | https://purl.org/rdm/ontology/Preserve                                                                                                                |
| rdfs:comment    | An act of saving and storing Resource to Repository, SoftwareApplication etc.<br>Resource を Repository, SoftwareApplication などに保存・保管する行動 |
| rdfs:subClassOf | rdm:Activity                                                                                                                                          |
| activityObject  | rdm:Resource                                                                                                                                          |
| agent           | rdm:Person                                                                                                                                            |
| example         | 研究者が、実験データを研究室の PC に保存する                                                                                                          |

|                 | rdm:Archive                                                    |
| --------------- | -------------------------------------------------------------- |
| URI             | https://purl.org/rdm/ontology/Archive                          |
| rdfs:comment    | An act of archiving Resource.<br>Resource をアーカイブする行動 |
| rdfs:subClassOf | rdm:Preserve                                                   |
| example         | 研究者が、会議発表資料をリポジトリにアーカイブする             |

|                 | rdm:Publish                                                                                                                                                                                                             |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| URI             | https://purl.org/rdm/ontology/Publish                                                                                                                                                                                   |
| rdfs:comment    | An act of making Resource public, such as by pushing "publish" button on publishing service. (including Resource of any access rights)<br>公開ボタンを押すなどして、Resource を公開する行動(アクセス権の種類は問わない) |
| rdfs:subClassOf | rdm:Activity                                                                                                                                                                                                            |
| activityObject  | rdm:Collection, rdm:Project, rdm:Resource                                                                                                                                                                               |
| example         | リポジトリ担当者が、リポジトリに登録された研究データの公開設定を「公開」に変更し、誰でもアクセスできる状態にする                                                                                                        |

|                 | rdm:Register                                                                                                                                                              |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| URI             | https://purl.org/rdm/ontology/Register                                                                                                                                    |
| rdfs:comment    | An act of registering Resource to Repository, SoftwareApplication or other service.<br>Repository, SoftwareApplication もしくはその他サービスに、 Resource を登録する行動 |
| rdfs:subClassOf | rdm:Activity                                                                                                                                                              |
| activityObject  | rdm:Collection, rdm:Resource                                                                                                                                              |
| example         | データ管理者が、リポジトリに公開したいデータセットを登録する                                                                                                              |

|                 | rdm:Reject                                                                                                                               |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| URI             | https://purl.org/rdm/ontology/Reject                                                                                                     |
| rdfs:comment    | An act of rejecting proposal/assigned role/submitted Resource etc.<br>提出された Resource や提案、割り当てられた役割などを取り下げる行動 |
| rdfs:subClassOf | rdm:Activity                                                                                                                             |
| activityObject  | rdm:Role                                                                                                                                 |
| example         | キュレーターが、自身に割り当てられたキュレーションタスクの担当者を降りる                                                                 |

|                 | rdm:Rename                                                    |
| --------------- | ------------------------------------------------------------- |
| URI             | https://purl.org/rdm/ontology/Rename                          |
| rdfs:comment    | An act of renaming Resource.<br>Resource の名称を変更する行動 |
| rdfs:subClassOf | rdm:Activity                                                  |
| activityObject  | rdm:Resource                                                  |
| agent           | rdm:Person                                                    |
| result          | rdm:Resource                                                  |
| example         | キュレーターが、ファイルの名前をルールに従うように変更する    |

|                 | rdm:Reorganize                                                                          |
| --------------- | --------------------------------------------------------------------------------------- |
| URI             | https://purl.org/rdm/ontology/Reorganize                                                |
| rdfs:comment    | An act of changing folder structure of Dataset.<br>Dataset のフォルダ構成を変更する行動 |
| rdfs:subClassOf | rdm:Activity                                                                            |
| activityObject  | rdm:Dataset                                                                             |
| agent           | rdm:Person                                                                              |
| result          | rdm:Dataset                                                                             |
| example         | キュレーターが、提出されたデータセットのフォルダ構成を bagit に合わせて変更する         |

|                 | rdm:Restructure                                                                                                                                                        |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| URI             | https://purl.org/rdm/ontology/Restructure                                                                                                                              |
| rdfs:comment    | An act of re-structuring Resource as part of data curation, such as sorting a table.<br>表データをソートするなど、キュレーションの一環として Resource を再構成する行動 |
| rdfs:subClassOf | rdm:Activity                                                                                                                                                           |
| activityObject  | rdm:Resource                                                                                                                                                           |
| agent           | rdm:Person                                                                                                                                                             |
| result          | rdm:Resource                                                                                                                                                           |
| example         | キュレーターが、キュレーション業務の一環として、提出されたデータのソート順を変更する                                                                                   |

|                 | rdm:Schedule                                                              |
| --------------- | ------------------------------------------------------------------------- |
| URI             | https://purl.org/rdm/ontology/Schedule                                    |
| rdfs:comment    | An act of scheduling future Event.<br>未来に行われる Event を設定する行動 |
| rdfs:subClassOf | rdm:Activity                                                              |
| activityObject  | rdm:Event                                                                 |
| example         | 研究者が、プロジェクトの全体会議を設定する                                |

|                 | rdm:Search                                                                                                         |
| --------------- | ------------------------------------------------------------------------------------------------------------------ |
| URI             | https://purl.org/rdm/ontology/Search                                                                               |
| rdfs:comment    | An act of searching Resource, such as by pushing "search" button.<br>検索ボタンの押下など、Resource を検索する行動 |
| rdfs:subClassOf | rdm:Activity                                                                                                       |
| activityObject  | rdm:Collection, rdm:Repository                                                                                     |
| agent           | rdm:Person                                                                                                         |
| result          | rdm:Resource                                                                                                       |
| example         | 研究者が、CiNii で先行研究の論文を検索する                                                                         |

|                 | rdm:Select                                                                                                                             |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| URI             | https://purl.org/rdm/ontology/Select                                                                                                   |
| rdfs:comment    | An act of selecting from options.<br>選択肢の中から利用するものを選択する行動                                                          |
| rdfs:subClassOf | rdm:Activity                                                                                                                           |
| activityObject  | rdm:Repository, rdm:Resource                                                                                                           |
| agent           | rdm:Person                                                                                                                             |
| example         | 研究者が、GRDM から WEKO にエクスポートする対象となるファイルを選択する<br>研究者が、GRDM でアドオンとして追加するストレージを選択する |

|                 | rdm:Send                                                                   |
| --------------- | -------------------------------------------------------------------------- |
| URI             | https://purl.org/rdm/ontology/Send                                         |
| rdfs:comment    | An act of dispatching Resource.<br>Resource を送る行動                     |
| rdfs:subClassOf | rdm:Activity                                                               |
| activityObject  | rdm:Resource                                                               |
| agent           | rdm:Person                                                                 |
| example         | データコーディネイターが、評価が終了した提出データをリポジトリ管理者に送る |

|                 | rdm:Suggest                                                        |
| --------------- | ------------------------------------------------------------------ |
| URI             | https://purl.org/rdm/ontology/Suggest                              |
| rdfs:comment    | An act of presenting or proposing options.<br>選択肢を提示する行動 |
| rdfs:subClassOf | rdm:Activity                                                       |
| activityObject  | rdm:Message                                                        |
| agent           | rdm:Person                                                         |
| example         | PI が、研究プロジェクトで利用するストレージを提案する              |

|                 | rdm:Update                                                                                        |
| --------------- | ------------------------------------------------------------------------------------------------- |
| URI             | https://purl.org/rdm/ontology/Update                                                              |
| rdfs:comment    | An act of updating an existing Resource with changes.<br>既存の Resource に変更を加え更新する行動 |
| rdfs:subClassOf | rdm:Activity                                                                                      |
| activityObject  | rdm:Resource                                                                                      |
| agent           | rdm:Person                                                                                        |
| result          | rdm:Resource                                                                                      |
| example         | 研究者が、DMP を更新する<br>キュレーターが、提出されたメタデータを編集して更新する                |

|                 | rdm:Upload                                                                                                                                     |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| URI             | https://purl.org/rdm/ontology/Upload                                                                                                           |
| rdfs:comment    | An act of uploading Resource to Repository, SoftwareApplication etc.<br>Resource を SoftwareApplication や Repository 等にアップロードする行動 |
| rdfs:subClassOf | rdm:Activity                                                                                                                                   |
| activityObject  | rdm:Resource                                                                                                                                   |
| agent           | rdm:Person                                                                                                                                     |
| example         | 研究者が、ローカル PC 内の研究データをクラウドストレージにアップロードする                                                                     |

|                 | rdm:Visualize                                                                                                                 |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| URI             | https://purl.org/rdm/ontology/Visualize                                                                                       |
| rdfs:comment    | An act of creating a visualization based on data, such as making a graph.<br>グラフを生成するなど、データを元に可視化する行動 |
| rdfs:subClassOf | rdm:Activity                                                                                                                  |
| activityObject  | rdm:Resource                                                                                                                  |
| agent           | rdm:Person                                                                                                                    |
| result          | rdm:Image, rdm:Video                                                                                                          |
| example         | 研究者が、 Matplotlib を利用して、数値データをグラフ化する                                                                    |

|              | rdm:Actor                                                                                              |
| ------------ | ------------------------------------------------------------------------------------------------------ |
| URI          | https://purl.org/rdm/ontology/Actor                                                                    |
| rdfs:comment | Person or organization that is the subject of the Activity.<br>Activity を行う主語にあたる人または組織 |

|                 | rdm:Institution                           |
| --------------- | ----------------------------------------- |
| URI             | https://purl.org/rdm/ontology/Institution |
| rdfs:comment    | An organization.<br>機関や組織            |
| rdfs:subClassOf | rdm:Actor                                 |

|                 | rdm:FundingAgency                                                   |
| --------------- | ------------------------------------------------------------------- |
| URI             | https://purl.org/rdm/ontology/FundingAgency                         |
| rdfs:comment    | An organization that funds research activities.<br>研究資金提供機関 |
| rdfs:subClassOf | rdm:Institution                                                     |

|                 | rdm:Person                           |
| --------------- | ------------------------------------ |
| URI             | https://purl.org/rdm/ontology/Person |
| rdfs:comment    | A person.<br>人物                    |
| rdfs:subClassOf | rdm:Actor                            |

|              | rdm:Object                                                                         |
| ------------ | ---------------------------------------------------------------------------------- |
| URI          | https://purl.org/rdm/ontology/Object                                               |
| rdfs:comment | Things and objects that are the object of Activity.<br>Activity の目的語となる事物 |

|                 | rdm:Collection                                       |
| --------------- | ---------------------------------------------------- |
| URI             | https://purl.org/rdm/ontology/Collection             |
| rdfs:comment    | A collection of items.<br>オブジェクトのコレクション |
| rdfs:subClassOf | rdm:Object                                           |

|                 | rdm:DataManagementPlan                                                                                                                                                                                                                       |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| URI             | https://purl.org/rdm/ontology/DataManagementPlan                                                                                                                                                                                             |
| rdfs:comment    | A data management plan (DMP).<br>データ管理計画(DMP)                                                                                                                                                                                         |
| rdfs:subClassOf | rdm:Object                                                                                                                                                                                                                                   |
| note            | This class corresponds to a set of data manager, access rights, license and so on, such as a single row in DMP format. Multiple instance of this class can be linked to a rdm:Project class to describe several set of data management plan. |

|                 | rdm:Event                                                        |
| --------------- | ---------------------------------------------------------------- |
| URI             | https://purl.org/rdm/ontology/Event                              |
| rdfs:comment    | An event, such as conferences etc.<br>学会など、イベントや催し物 |
| rdfs:subClassOf | rdm:Object                                                       |

|                 | rdm:Experiment                           |
| --------------- | ---------------------------------------- |
| URI             | https://purl.org/rdm/ontology/Experiment |
| rdfs:comment    | Experiment.<br>実験                      |
| rdfs:subClassOf | rdm:Object                               |

|                 | rdm:Grant                                              |
| --------------- | ------------------------------------------------------ |
| URI             | https://purl.org/rdm/ontology/Grant                    |
| rdfs:comment    | A grant for research activities.<br>研究資金プログラム |
| rdfs:subClassOf | rdm:Object                                             |

|                 | rdm:Identifier                           |
| --------------- | ---------------------------------------- |
| URI             | https://purl.org/rdm/ontology/Identifier |
| rdfs:comment    | An identifier.<br>識別子                 |
| rdfs:subClassOf | rdm:Object                               |

|                 | rdm:Intangible                                                                        |
| --------------- | ------------------------------------------------------------------------------------- |
| URI             | https://purl.org/rdm/ontology/Intangible                                              |
| rdfs:comment    | Abstract class for concepts without entities.<br>実体を伴わない概念のための抽象クラス |
| rdfs:subClassOf | rdm:Object                                                                            |

|                 | rdm:Role                           |
| --------------- | ---------------------------------- |
| URI             | https://purl.org/rdm/ontology/Role |
| rdfs:comment    | Roles and positions.<br>役割、役職 |
| rdfs:subClassOf | rdm:Intangible                     |

|                 | rdm:Project                             |
| --------------- | --------------------------------------- |
| URI             | https://purl.org/rdm/ontology/Project   |
| rdfs:comment    | A research project.<br>研究プロジェクト |
| rdfs:subClassOf | rdm:Object                              |

|                 | rdm:Repository                           |
| --------------- | ---------------------------------------- |
| URI             | https://purl.org/rdm/ontology/Repository |
| rdfs:comment    | A repository.<br>リポジトリ              |
| rdfs:subClassOf | rdm:Object                               |

|                 | rdm:Resource                                                                                                         |
| --------------- | -------------------------------------------------------------------------------------------------------------------- |
| URI             | https://purl.org/rdm/ontology/Resource                                                                               |
| rdfs:comment    | A digital object, such as research data, video of experiments rtc.<br>研究データや実験動画など、デジタルオブジェクト |
| rdfs:subClassOf | rdm:Object                                                                                                           |

|                 | rdm:Audio                           |
| --------------- | ----------------------------------- |
| URI             | https://purl.org/rdm/ontology/Audio |
| rdfs:comment    | An audio file.<br>音声              |
| rdfs:subClassOf | rdm:Resource                        |

|                 | rdm:Book                           |
| --------------- | ---------------------------------- |
| URI             | https://purl.org/rdm/ontology/Book |
| rdfs:comment    | A book.<br>書籍                    |
| rdfs:subClassOf | rdm:Resource                       |

|                 | rdm:ConferenceObject                                                   |
| --------------- | ---------------------------------------------------------------------- |
| URI             | https://purl.org/rdm/ontology/ConferenceObject                         |
| rdfs:comment    | A Resource related to conferences.<br>カンファレンスに関連するリソース |
| rdfs:subClassOf | rdm:Resource                                                           |

|                 | rdm:ConferencePaper                           |
| --------------- | --------------------------------------------- |
| URI             | https://purl.org/rdm/ontology/ConferencePaper |
| rdfs:comment    | A conference paper.<br>カンファレンスペーパー |
| rdfs:subClassOf | rdm:Resource                                  |

|                 | rdm:ConferenceProceeding                                   |
| --------------- | ---------------------------------------------------------- |
| URI             | https://purl.org/rdm/ontology/ConferenceProceeding         |
| rdfs:comment    | A conference proceeding.<br>カンファレンスプロシーディング |
| rdfs:subClassOf | rdm:Resource                                               |

|                 | rdm:Dataset                           |
| --------------- | ------------------------------------- |
| URI             | https://purl.org/rdm/ontology/Dataset |
| rdfs:comment    | A dataset.<br>データセット            |
| rdfs:subClassOf | rdm:Resource                          |

|                 | rdm:EducationalResource                                                        |
| --------------- | ------------------------------------------------------------------------------ |
| URI             | https://purl.org/rdm/ontology/EducationalResource                              |
| rdfs:comment    | A Resource related to educational, such as slides for lecture.<br>教育関連資料 |
| rdfs:subClassOf | rdm:Resource                                                                   |

|                 | rdm:Image                           |
| --------------- | ----------------------------------- |
| URI             | https://purl.org/rdm/ontology/Image |
| rdfs:comment    | An image file.<br>画像              |
| rdfs:subClassOf | rdm:Resource                        |

|                 | rdm:Journal                           |
| --------------- | ------------------------------------- |
| URI             | https://purl.org/rdm/ontology/Journal |
| rdfs:comment    | A journal.<br>ジャーナル              |
| rdfs:subClassOf | rdm:Resource                          |

|                 | rdm:JournalArticle                                   |
| --------------- | ---------------------------------------------------- |
| URI             | https://purl.org/rdm/ontology/JournalArticle         |
| rdfs:comment    | An article published in a journal.<br>ジャーナル論文 |
| rdfs:subClassOf | rdm:Resource                                         |

|                 | rdm:Message                                  |
| --------------- | -------------------------------------------- |
| URI             | https://purl.org/rdm/ontology/Message        |
| rdfs:comment    | Message and comment.<br>メッセージやコメント |
| rdfs:subClassOf | rdm:Resource                                 |

|                 | rdm:MetadataDocument                                     |
| --------------- | -------------------------------------------------------- |
| URI             | https://purl.org/rdm/ontology/MetadataDocument           |
| rdfs:comment    | Metadata of any Resource.<br>Resource に関するメタデータ |
| rdfs:subClassOf | rdm:Resource                                             |

|                 | rdm:Preprint                           |
| --------------- | -------------------------------------- |
| URI             | https://purl.org/rdm/ontology/Preprint |
| rdfs:comment    | A preprint.<br>プレプリント            |
| rdfs:subClassOf | rdm:Resource                           |

|                 | rdm:Report                           |
| --------------- | ------------------------------------ |
| URI             | https://purl.org/rdm/ontology/Report |
| rdfs:comment    | A report.<br>レポート、報告書        |
| rdfs:subClassOf | rdm:Resource                         |

|                 | rdm:Review                                              |
| --------------- | ------------------------------------------------------- |
| URI             | https://purl.org/rdm/ontology/Review                    |
| rdfs:comment    | Review documents and evaluations.<br>レビュー文書や評価 |
| rdfs:subClassOf | rdm:Resource                                            |

|                 | rdm:Standard                           |
| --------------- | -------------------------------------- |
| URI             | https://purl.org/rdm/ontology/Standard |
| rdfs:comment    | A standard.<br>標準                    |
| rdfs:subClassOf | rdm:Resource                           |

|                 | rdm:Thesis                           |
| --------------- | ------------------------------------ |
| URI             | https://purl.org/rdm/ontology/Thesis |
| rdfs:comment    | A thesis.<br>学位論文                |
| rdfs:subClassOf | rdm:Resource                         |

|                 | rdm:Video                           |
| --------------- | ----------------------------------- |
| URI             | https://purl.org/rdm/ontology/Video |
| rdfs:comment    | A video file.<br>動画               |
| rdfs:subClassOf | rdm:Resource                        |

|                 | rdm:Workflow                           |
| --------------- | -------------------------------------- |
| URI             | https://purl.org/rdm/ontology/Workflow |
| rdfs:comment    | A workflow.<br>ワークフロー            |
| rdfs:subClassOf | rdm:Resource                           |

|                 | rdm:OtherResource                                                              |
| --------------- | ------------------------------------------------------------------------------ |
| URI             | https://purl.org/rdm/ontology/OtherResource                                    |
| rdfs:comment    | An other Resource.<br>その他のリソース                                         |
| rdfs:subClassOf | rdm:Resource                                                                   |
| rdfs:subClassOf | rdm:Object                                                                     |
| note            | This class can be used only when no other subclass of Resource is appropriate. |

|                 | rdm:RightsStatement                                                                             |
| --------------- | ----------------------------------------------------------------------------------------------- |
| URI             | https://purl.org/rdm/ontology/RightsStatement                                                   |
| rdfs:comment    | A higer-level class that relates to various rights.<br>権利関係全般に関連するクラス             |
| rdfs:subClassOf | rdm:Object                                                                                      |
| note            | This class is only used as a super-class of rdm:AccessRights and rdm:License, not for instance. |

|                 | rdm:AccessRights                                                                                                                                                               |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| URI             | https://purl.org/rdm/ontology/AccessRights                                                                                                                                     |
| rdfs:comment    | An access right o Resource.<br>リソースへのアクセス権                                                                                                                          |
| rdfs:subClassOf | rdm:RightsStatement                                                                                                                                                            |
| note            | A value of property rdm:conditionOfAccess is required.<br> A value of property rdm:dateAvailable is required when the value of rdm:conditionOfAccess is _rdm:EmbargoedAccess_. |

|                 | rdm:License                                    |
| --------------- | ---------------------------------------------- |
| URI             | https://purl.org/rdm/ontology/License          |
| rdfs:comment    | A license of Resource.<br>リソースのライセンス |
| rdfs:subClassOf | rdm:RightsStatement                            |
| note            | A value of property rdm:url is required.       |

|                 | rdm:SoftwareApplication                                 |
| --------------- | ------------------------------------------------------- |
| URI             | https://purl.org/rdm/ontology/SoftwareApplication       |
| rdfs:comment    | A software application.<br>ソフトウェアアプリケーション |
| rdfs:subClassOf | rdm:Object                                              |

## Properties

### ObjectProperty

|              | rdm:accessRightsInformation                                               |
| ------------ | ------------------------------------------------------------------------- |
| URI          | https://purl.org/rdm/ontology/accessRightsInformation                     |
| rdf:type     | ObjectProperty                                                            |
| rdfs:comment | Information on access rights of this Class.<br>クラスのアクセス権関連情報 |
| rdfs:domain  | rdm:Project, rdm:Resource                                                 |
| rdfs:range   | rdm:AccessRights                                                          |

|                    | rdm:dataAccessRightsInformation                                                                              |
| ------------------ | ------------------------------------------------------------------------------------------------------------ |
| URI                | https://purl.org/rdm/ontology/dataAccessRightsInformation                                                    |
| rdf:type           | ObjectProperty                                                                                               |
| rdfs:subPropertyOf | rdm:accessRightsInformation                                                                                  |
| rdfs:comment       | Information on access rights to be described in this DataManagementPlan.<br>DMP におけるデータへのアクセス権 |
| rdfs:domain        | rdm:DataManagementPlan                                                                                       |

|              | rdm:activityObject                                                                                                      |
| ------------ | ----------------------------------------------------------------------------------------------------------------------- |
| URI          | https://purl.org/rdm/ontology/activityObject                                                                            |
| rdf:type     | ObjectProperty                                                                                                          |
| rdfs:comment | An object of the Activity.<br>行動の対象物                                                                              |
| rdfs:domain  | rdm:Activity                                                                                                            |
| rdfs:range   | rdm:Collection, rdm:Event, rdm:Experiment, rdm:Project, rdm:Repository, rdm:Resource, rdm:Role, rdm:SoftwareApplication |

|              | rdm:affiliation                                                          |
| ------------ | ------------------------------------------------------------------------ |
| URI          | https://purl.org/rdm/ontology/affiliation                                |
| rdf:type     | ObjectProperty                                                           |
| rdfs:comment | An organization that this Person is affiliated with.<br>人物の所属先機関 |
| rdfs:domain  | rdm:Person                                                               |
| rdfs:range   | rdm:Institution                                                          |

|              | rdm:agent                                                                      |
| ------------ | ------------------------------------------------------------------------------ |
| URI          | https://purl.org/rdm/ontology/agent                                            |
| rdf:type     | ObjectProperty                                                                 |
| rdfs:comment | The direct performer or driver of this Activity.<br>行動・行為の直接的な実施者 |
| rdfs:domain  | rdm:Activity                                                                   |
| rdfs:range   | rdm:Person, rdm:Institution                                                    |

|               | rdm:collectedIn                                                                                                 |
| ------------- | --------------------------------------------------------------------------------------------------------------- |
| URI           | https://purl.org/rdm/ontology/collectedIn                                                                       |
| rdf:type      | ObjectProperty                                                                                                  |
| rdfs:comment  | A Collection which includes this Resource as a member of Collection.<br>リソースをメンバーとして含む Collection |
| owl:inverseOf | rdm:collectionItem                                                                                              |
| rdfs:domain   | rdm:Resource                                                                                                    |
| rdfs:range    | rdm:Collection                                                                                                  |

|              | rdm:conditionOfAccess                           |
| ------------ | ----------------------------------------------- |
| URI          | https://purl.org/rdm/ontology/conditionOfAccess |
| rdf:type     | ObjectProperty                                  |
| rdfs:comment | Access rights type.<br>アクセス権の種別         |
| rdfs:domain  | rdm:AccessRights                                |
| rdfs:range   | rdm:RightStatement                              |

|              | rdm:contributor                                                                               |
| ------------ | --------------------------------------------------------------------------------------------- |
| URI          | https://purl.org/rdm/ontology/contributor                                                     |
| rdf:type     | ObjectProperty                                                                                |
| rdfs:comment | A contributor to this Class.<br>クラスへの寄与者                                              |
| rdfs:domain  | rdm:Collection, rdm:Event, rdm:Experiment, rdm:Project, rdm:Resource, rdm:SoftwareApplication |
| rdfs:range   | rdm:Person, rdm:Institution                                                                   |
| note         | This property can be used only when no other subproperty of this property is appropriate.     |

|                    | rdm:creator                                               |
| ------------------ | --------------------------------------------------------- |
| URI                | https://purl.org/rdm/ontology/creator                     |
| rdf:type           | ObjectProperty                                            |
| rdfs:subPropertyOf | rdm:contributor                                           |
| rdfs:comment       | The creator/author of this Resource. <br>リソースの作成者 |
| rdfs:domain        | rdm:Resource, rdm:SoftwareApplication                     |
| rdfs:range         | rdm:Person                                                |

|                    | rdm:dataCreator                                                                                            |
| ------------------ | ---------------------------------------------------------------------------------------------------------- |
| URI                | https://purl.org/rdm/ontology/dataCreater                                                                  |
| rdf:type           | ObjectProperty                                                                                             |
| rdfs:subPropertyOf | rdm:creator                                                                                                |
| rdfs:comment       | The creator of research data to be described in this DataManagementPlan.<br>DMP における研究データの作成者 |
| rdfs:domain        | rdm:DataManagementPlan                                                                                     |
| rdfs:range         | rdm:Person                                                                                                 |

|                    | rdm:dataManager                                                                                               |
| ------------------ | ------------------------------------------------------------------------------------------------------------- |
| URI                | https://purl.org/rdm/ontology/dataManager                                                                     |
| rdf:type           | ObjectProperty                                                                                                |
| rdfs:subPropertyOf | rdm:contributor                                                                                               |
| rdfs:comment       | The data manager of research data to be described in this DataManagementPlan.<br>DMP における研究データ管理者 |
| rdfs:domain        | rdm:DataManagementPlan                                                                                        |
| rdfs:range         | rdm:Person                                                                                                    |

|                    | rdm:experimenter                                                                      |
| ------------------ | ------------------------------------------------------------------------------------- |
| URI                | https://purl.org/rdm/ontology/experimenter                                            |
| rdf:type           | ObjectProperty                                                                        |
| rdfs:subPropertyOf | rdm:contributor                                                                       |
| rdfs:comment       | The practitioner, performer and executor of this Experiment. <br>実験の実施者、実行者 |
| rdfs:domain        | rdm:Experiment                                                                        |
| rdfs:range         | rdm:Person                                                                            |

|                    | rdm:hostingInstitution                                                                                                                                                                           |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| URI                | https://purl.org/rdm/ontology/hostingInstitution                                                                                                                                                 |
| rdf:type           | ObjectProperty                                                                                                                                                                                   |
| rdfs:subPropertyOf | rdm:contributor                                                                                                                                                                                  |
| rdfs:comment       | The hosting institution of Resource (in Project) and research data to be described in this DataManagementPlan.<br>(Project に属する)Resource の管理機関、もしくは DMP における研究データ管理機関 |
| rdfs:domain        | rdm:Project, rdm:Resource, rdm:DataManagementPlan                                                                                                                                                |
| rdfs:range         | rdm:Institution                                                                                                                                                                                  |

|                    | rdm:identifierManager                                                                                           |
| ------------------ | --------------------------------------------------------------------------------------------------------------- |
| URI                | https://purl.org/rdm/ontology/identifierManager                                                                 |
| rdf:type           | ObjectProperty                                                                                                  |
| rdfs:subPropertyOf | rdm:contributor                                                                                                 |
| rdfs:comment       | A manager of identifier scheme/service, e.g. International DOI Foundation.<br>国際 DOI 財団など、識別子の管理者 |
| rdfs:domain        | rdm:Identifier                                                                                                  |
| rdfs:range         | rdm:Institution                                                                                                 |

|                    | rdm:organizer                                           |
| ------------------ | ------------------------------------------------------- |
| URI                | https://purl.org/rdm/ontology/organizer                 |
| rdf:type           | ObjectProperty                                          |
| rdfs:subPropertyOf | rdm:contributor                                         |
| rdfs:comment       | An Event organizer or host.<br>イベントの開催者、主催者 |
| rdfs:domain        | rdm:Event                                               |

|                    | rdm:researcher                                                         |
| ------------------ | ---------------------------------------------------------------------- |
| URI                | https://purl.org/rdm/ontology/researcher                               |
| rdf:type           | ObjectProperty                                                         |
| rdfs:subPropertyOf | rdm:contributor                                                        |
| rdfs:comment       | A researcher involved in this Project.<br>プロジェクトに参加した研究者 |
| rdfs:domain        | rdm:Project                                                            |
| rdfs:range         | rdm:Person                                                             |

|              | rdm:dmp                                                                                                |
| ------------ | ------------------------------------------------------------------------------------------------------ |
| URI          | https://purl.org/rdm/ontology/dmp                                                                      |
| rdf:type     | ObjectProperty                                                                                         |
| rdfs:comment | Contents of data management plan of this Project/Resource.<br>資源やプロジェクトに紐づくデータ管理計画 |
| rdfs:domain  | rdm:Resource, rdm:Project                                                                              |
| rdfs:range   | rdm:DataManagementPlan                                                                                 |

|              | rdm:dmpFormatProvider                                                            |
| ------------ | -------------------------------------------------------------------------------- |
| URI          | https://purl.org/rdm/ontology/dmpFormatProvider                                  |
| rdf:type     | ObjectProperty                                                                   |
| rdfs:comment | A institution which provides this DataManagementPlan format.<br>DMP 種別の提供者 |
| rdfs:domain  | rdm:DataManagementPlan                                                           |
| rdfs:range   | rdm:Institution                                                                  |

|              | rdm:funder                                                                                                          |
| ------------ | ------------------------------------------------------------------------------------------------------------------- |
| URI          | https://purl.org/rdm/ontology/funder                                                                                |
| rdf:type     | ObjectProperty                                                                                                      |
| rdfs:comment | An organization that funds this Project or research activities to create this Resource.<br>研究資金プログラム提供者 |
| rdfs:domain  | rdm:Resource, rdm:Project, rdm:Grant                                                                                |
| rdfs:range   | rdm:FundingAgency                                                                                                   |

|              | rdm:funding                                                                                            |
| ------------ | ------------------------------------------------------------------------------------------------------ |
| URI          | https://purl.org/rdm/ontology/funding                                                                  |
| rdf:type     | ObjectProperty                                                                                         |
| rdfs:comment | A grant program for this Project or research activities to create this Resource.<br>研究資金プログラム |
| rdfs:domain  | rdm:Resource, rdm:Project                                                                              |
| rdfs:range   | rdm:Grant                                                                                              |

|              | rdm:identifierInformation                                                |
| ------------ | ------------------------------------------------------------------------ |
| URI          | https://purl.org/rdm/ontology/identifierInformation                      |
| rdf:type     | ObjectProperty                                                           |
| rdfs:comment | An identifier information of this Class.<br>識別子                       |
| rdfs:domain  | rdm:Resource, Repository, Project, Collection, Person, Institution,Grant |
| rdfs:range   | rdm:Identifier                                                           |

|                    | rdm:dataIdentifier                                                                                      |
| ------------------ | ------------------------------------------------------------------------------------------------------- |
| URI                | https://purl.org/rdm/ontology/dataIdentifier                                                            |
| rdf:type           | ObjectProperty                                                                                          |
| rdfs:subPropertyOf | rdm:identifierInformation                                                                               |
| rdfs:comment       | The identifier of research data to be described in this DataManagementPlan.<br>DMP におけるデータ識別子 |
| rdfs:domain        | rdm:DataManagementPlan                                                                                  |
| rdfs:range         | rdm:Identifier                                                                                          |

|              | rdm:inclusionRelation                                                                                                                  |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------- |
| URI          | https://purl.org/rdm/ontology/inclusionRelation                                                                                        |
| rdf:type     | ObjectProperty                                                                                                                         |
| rdfs:comment | A higher-level property that indicates inclusion relationship between Classes.<br>主語クラスと包含関係のあるクラスを指す上位プロパティ |
| note         | This class is only used as a super-class of properties indicating overlap between classes, not for instance.                           |

|                    | rdm:hasPart                                                                                                                     |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------- |
| URI                | https://purl.org/rdm/ontology/hasPart                                                                                           |
| rdf:type           | ObjectProperty                                                                                                                  |
| rdfs:subPropertyOf | rdm:inclusionRelation                                                                                                           |
| rdfs:comment       | A class consisting of multiple parts of which this class is a part.<br>主語クラスが一部分となっている、複数の部分から成るクラス |
| owl:inverseOf      | rdm:isPartOf                                                                                                                    |
| rdfs:domain        | rdm:Project, rdm:Resource, rdm:Collection, rdm:Institution, rdm:SoftwareApplication, rdm:Grant, rdm:Experiment                  |

|                    | rdm:isPartOf                                                                                                   |
| ------------------ | -------------------------------------------------------------------------------------------------------------- |
| URI                | https://purl.org/rdm/ontology/isPartOf                                                                         |
| rdf:type           | ObjectProperty                                                                                                 |
| rdfs:subPropertyOf | rdm:inclusionRelation                                                                                          |
| rdfs:comment       | A Class of the parts that make up this class<br>主語クラスを構成する部分のクラス                               |
| owl:inverseOf      | rdm:hasPart                                                                                                    |
| rdfs:domain        | rdm:Project, rdm:Resource, rdm:Collection, rdm:Institution, rdm:SoftwareApplication, rdm:Grant, rdm:Experiment |

|               | rdm:inProject                                                                  |
| ------------- | ------------------------------------------------------------------------------ |
| URI           | https://purl.org/rdm/ontology/inProject                                        |
| rdf:type      | ObjectProperty                                                                 |
| rdfs:comment  | A Project this Resource is within/included in.<br>リソースが属するプロジェクト |
| owl:inverseOf | rdm:projectItem                                                                |
| rdfs:domain   | rdm:Resource                                                                   |
| rdfs:range    | rdm:Project                                                                    |

|              | rdm:instrument                                                                       |
| ------------ | ------------------------------------------------------------------------------------ |
| URI          | https://purl.org/rdm/ontology/instrument                                             |
| rdf:type     | ObjectProperty                                                                       |
| rdfs:comment | The object that helped the agent perform the Activity.<br>行動を補助した道具、ツール |
| rdfs:domain  | rdm:Activity, rdm:Experiment                                                         |

|              | rdm:isRelatedTo                                                                                                                                               |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| URI          | https://purl.org/rdm/ontology/isRelatedTo                                                                                                                     |
| rdf:type     | ObjectProperty                                                                                                                                                |
| rdfs:comment | A Class independent of this Class that is related to this Class.<br>主語クラスと何らかの関連がある、独立したクラス                                            |
| note         | This property is used to relationship between classes that are independent of each other. (There is no overlap.) Cannot be used to link subject class itself. |

|                    | rdm:cites                                                                                        |
| ------------------ | ------------------------------------------------------------------------------------------------ |
| URI                | https://purl.org/rdm/ontology/cites                                                              |
| rdf:type           | ObjectProperty                                                                                   |
| rdfs:subPropertyOf | rdm:isRelatedTo                                                                                  |
| rdfs:comment       | A Resource that this Class cites.<br>主語クラスが引用しているリソース                            |
| owl:inverseOf      | rdm:isCitedBy                                                                                    |
| rdfs:domain        | rdm:Resource                                                                                     |
| rdfs:range         | rdm:Resource                                                                                     |
| rdfs:seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#cites |

|                    | rdm:collects                                                                                        |
| ------------------ | --------------------------------------------------------------------------------------------------- |
| URI                | https://purl.org/rdm/ontology/collects                                                              |
| rdf:type           | ObjectProperty                                                                                      |
| rdfs:subPropertyOf | rdm:isRelatedTo                                                                                     |
| rdfs:comment       | A Class which collected/created by using this Class.<br>主語クラスを使用して収集・作成されたクラス  |
| owl:inverseOf      | rdm:isCollectedBy                                                                                   |
| rdfs:domain        | rdm:Resource, rdm:Collection, rdm:SoftwareApplication                                               |
| rdfs:seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#collects |

|                    | rdm:compiles                                                                                                          |
| ------------------ | --------------------------------------------------------------------------------------------------------------------- |
| URI                | https://purl.org/rdm/ontology/compiles                                                                                |
| rdf:type           | ObjectProperty                                                                                                        |
| rdfs:subPropertyOf | rdm:isRelatedTo                                                                                                       |
| rdfs:comment       | The result of a compile or creation event using this Class.<br>主語クラスを使用したコンパイルまたは作成イベントの結果 |
| owl:inverseOf      | rdm:isCompiledBy                                                                                                      |
| rdfs:domain        | rdm:Resource, rdm:SoftwareApplication                                                                                 |
| rdfs:seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#compiles                   |

|                    | rdm:continues                                                                                        |
| ------------------ | ---------------------------------------------------------------------------------------------------- |
| URI                | https://purl.org/rdm/ontology/continues                                                              |
| rdf:type           | ObjectProperty                                                                                       |
| rdfs:subPropertyOf | rdm:isRelatedTo                                                                                      |
| rdfs:comment       | A Class of which this Class is a continuation.<br>主語クラスが継続しているクラス                     |
| owl:inverseOf      | rdm:isContinuedBy                                                                                    |
| rdfs:domain        | rdm:Institution, rdm:SoftwareApplication, rdm:Resource, rdm:Repository, rdm:Project, rdm:Event       |
| rdfs:seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#continues |

|                    | rdm:describes                                                                                        |
| ------------------ | ---------------------------------------------------------------------------------------------------- |
| URI                | https://purl.org/rdm/ontology/describes                                                              |
| rdf:type           | ObjectProperty                                                                                       |
| rdfs:subPropertyOf | rdm:isRelatedTo                                                                                      |
| rdfs:comment       | A Class that this Resource describes.<br>Resource が説明しているクラス                               |
| owl:inverseOf      | rdm:isDescribedBy                                                                                    |
| rdfs:domain        | rdm:Resource                                                                                         |
| rdfs:seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#continues |

|                    | rdm:documents                                                                                                                      |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------------- |
| URI                | https://purl.org/rdm/ontology/documents                                                                                            |
| rdf:type           | ObjectProperty                                                                                                                     |
| rdfs:subPropertyOf | rdm:isRelatedTo                                                                                                                    |
| rdfs:comment       | A SoftwareApplication which is documented by this Resource.<br>Resource がその説明文書・ドキュメントに相当する SoftwareApplication |
| owl:inverseOf      | rdm:isDocumentedBy                                                                                                                 |
| rdfs:domain        | rdm:Resource                                                                                                                       |
| rdfs:seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#documents                               |

|                    | rdm:hasMetadata                                                                                      |
| ------------------ | ---------------------------------------------------------------------------------------------------- |
| URI                | https://purl.org/rdm/ontology/hasMetadata                                                            |
| rdf:type           | ObjectProperty                                                                                       |
| rdfs:subPropertyOf | rdm:isRelatedTo                                                                                      |
| rdfs:comment       | A Resource which has additional metadata of this Class.<br>主語クラスの追加メタデータを持つ Resource |
| owl:inverseOf      | rdm:isMetadataFor                                                                                    |
| rdfs:range         | rdm:Resource                                                                                         |
| rdfs:seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#continues |

|                    | rdm:hasVersion                                                                                           |
| ------------------ | -------------------------------------------------------------------------------------------------------- |
| URI                | https://purl.org/rdm/ontology/hasVersion                                                                 |
| rdf:type           | ObjectProperty                                                                                           |
| rdfs:subPropertyOf | rdm:isRelatedTo                                                                                          |
| rdfs:comment       | A Class which is another version of this Class.<br>主語クラスの異なるバージョンとして存在するクラス      |
| owl:inverseOf      | rdm:isVersionOf                                                                                          |
| rdfs:domain        | rdm:Resource, rdm:Collection, rdm:SoftwareApplication                                                    |
| rdfs:range         | rdm:Resource, rdm:Collection, rdm:SoftwareApplication                                                    |
| rdfs:seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#ismetadatafor |

|                    | rdm:isCitedBy                                                                                        |
| ------------------ | ---------------------------------------------------------------------------------------------------- |
| URI                | https://purl.org/rdm/ontology/isCitedBy                                                              |
| rdf:type           | ObjectProperty                                                                                       |
| rdfs:subPropertyOf | rdm:isRelatedTo                                                                                      |
| rdfs:comment       | A Resource that this Class is cited.<br>主語クラスが引用されているリソース                           |
| owl:inverseOf      | rdm:cites                                                                                            |
| rdfs:domain        | rdm:Resource                                                                                         |
| rdfs:range         | rdm:Resource                                                                                         |
| rdfs:seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#iscitedby |

|                    | rdm:isCollectedBy                                                                                        |
| ------------------ | -------------------------------------------------------------------------------------------------------- |
| URI                | https://purl.org/rdm/ontology/isCollectedBy                                                              |
| rdf:type           | ObjectProperty                                                                                           |
| rdfs:subPropertyOf | rdm:isRelatedTo                                                                                          |
| rdfs:comment       | A Class that is used to collect/create this Class.<br>主語クラスの収集・生成に利用されたクラス           |
| owl:inverseOf      | rdm:collects                                                                                             |
| rdfs:domain        | rdm:Resource, rdm:Collection, rdm:SoftwareApplication                                                    |
| rdfs:seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#iscollectedby |

|                    | rdm:isCompiledBy                                                                                          |
| ------------------ | --------------------------------------------------------------------------------------------------------- |
| URI                | https://purl.org/rdm/ontology/isCompiledBy                                                                |
| rdf:type           | ObjectProperty                                                                                            |
| rdfs:subPropertyOf | rdm:isRelatedTo                                                                                           |
| rdfs:comment       | A Class used to compile or create this Class.<br>主語クラスをコンパイルまたは作成するために使用するクラス |
| owl:inverseOf      | rdm:compiles                                                                                              |
| rdfs:domain        | rdm:Resource, rdm:SoftwareApplication                                                                     |
| rdfs:seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#iscompiledby   |

|                    | rdm:isContinuedBy                                                                                        |
| ------------------ | -------------------------------------------------------------------------------------------------------- |
| URI                | https://purl.org/rdm/ontology/isContinuedBy                                                              |
| rdf:type           | ObjectProperty                                                                                           |
| rdfs:subPropertyOf | rdm:isRelatedTo                                                                                          |
| rdfs:comment       | A Class continued by this Class<br>主語クラスが継続されているクラス                                      |
| owl:inverseOf      | rdm:continues                                                                                            |
| rdfs:seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#iscontinuedby |

|                    | rdm:isDerivedFrom                                                                                        |
| ------------------ | -------------------------------------------------------------------------------------------------------- |
| URI                | https://purl.org/rdm/ontology/isDerivedFrom                                                              |
| rdf:type           | ObjectProperty                                                                                           |
| rdfs:subPropertyOf | rdm:isRelatedTo                                                                                          |
| rdfs:comment       | A Class on which this Class is based.<br>主語クラスが基づいているクラス                                  |
| owl:inverseOf      | rdm:isSourceOf                                                                                           |
| rdfs:range         | rdm:Project, rdm:Resource, rdm:Collection                                                                |
| rdfs:seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#isderivedfrom |

|                    | rdm:isDescribedBy                                                                                    |
| ------------------ | ---------------------------------------------------------------------------------------------------- |
| URI                | https://purl.org/rdm/ontology/isDescribedBy                                                          |
| rdf:type           | ObjectProperty                                                                                       |
| rdfs:subPropertyOf | rdm:isRelatedTo                                                                                      |
| rdfs:comment       | A Resource that describes this Class.<br>主語クラスを説明している Resource                           |
| owl:inverseOf      | rdm:describes                                                                                        |
| rdfs:seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#continues |

|                    | rdm:isDocumentedBy                                                                                                                          |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------- |
| URI                | https://purl.org/rdm/ontology/isDocumentedBy                                                                                                |
| rdf:type           | ObjectProperty                                                                                                                              |
| rdfs:subPropertyOf | rdm:isRelatedTo                                                                                                                             |
| rdfs:comment       | A Resource which is documentation about/explaining this SoftwareApplication.<br>SoftwareApplication の説明文書・ドキュメントである Resource |
| owl:inverseOf      | rdm:documents                                                                                                                               |
| rdfs:domain        | rdm:SoftwareApplication                                                                                                                     |
| rdfs:seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#isdocumentedby                                   |

|                    | rdm:isIdenticalTo                                                                                        |
| ------------------ | -------------------------------------------------------------------------------------------------------- |
| URI                | https://purl.org/rdm/ontology/isIdenticalTo                                                              |
| rdf:type           | ObjectProperty                                                                                           |
| rdfs:subPropertyOf | rdm:isRelatedTo                                                                                          |
| rdfs:comment       | A Resource which is identical to this Resource.<br>主語クラスと同一である Resource                       |
| rdfs:domain        | rdm:Resource                                                                                             |
| rdfs:seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#isidenticalto |

|                    | rdm:isMetadataFor                                                                                        |
| ------------------ | -------------------------------------------------------------------------------------------------------- |
| URI                | https://purl.org/rdm/ontology/isMetadataFor                                                              |
| rdf:type           | ObjectProperty                                                                                           |
| rdfs:subPropertyOf | rdm:isRelatedTo                                                                                          |
| rdfs:comment       | A Class for which this Resource has additional metadata.<br>Resource が追加メタデータになっているクラス  |
| owl:inverseOf      | rdm:hasMetadata                                                                                          |
| rdfs:domain        | rdm:Resource                                                                                             |
| rdfs:seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#ismetadatafor |

|                    | rdm:isNewVersionOf                                                                                        |
| ------------------ | --------------------------------------------------------------------------------------------------------- |
| URI                | https://purl.org/rdm/ontology/isNewVersionOf                                                              |
| rdf:type           | ObjectProperty                                                                                            |
| rdfs:subPropertyOf | rdm:isRelatedTo                                                                                           |
| rdfs:comment       | A Class which is a new edition of this Class.<br>主語クラスが新版に当たる、旧版のクラス                   |
| owl:inverseOf      | rdm:isPreviousVersionOf                                                                                   |
| rdfs:domain        | rdm:Resource, rdm:Collection, rdm:SoftwareApplication                                                     |
| rdfs:range         | rdm:Resource, rdm:Collection, rdm:SoftwareApplication                                                     |
| rdfs:seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#isnewversionof |

|                    | rdm:isObsoletedBy                                                                                        |
| ------------------ | -------------------------------------------------------------------------------------------------------- |
| URI                | https://purl.org/rdm/ontology/isObsoletedBy                                                              |
| rdf:type           | ObjectProperty                                                                                           |
| rdfs:subPropertyOf | rdm:isRelatedTo                                                                                          |
| rdfs:comment       | A Class which replaces this Class.<br>主語クラスを廃止させたクラス                                       |
| owl:inverseOf      | rdm:obsoletes                                                                                            |
| rdfs:seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#isobsoletedby |

|                    | rdm:isOriginalFormOf                                                                                        |
| ------------------ | ----------------------------------------------------------------------------------------------------------- |
| URI                | https://purl.org/rdm/ontology/isOriginalFormOf                                                              |
| rdf:type           | ObjectProperty                                                                                              |
| rdfs:subPropertyOf | rdm:isRelatedTo                                                                                             |
| rdfs:comment       | A Class of which this Class is the original form.<br>主語クラスをオリジナルとするクラス                     |
| owl:inverseOf      | rdm:isVariantFormOf                                                                                         |
| rdfs:domain        | rdm:Resource, rdm:SoftwareApplication                                                                       |
| rdfs:seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#isoriginalformof |

|                    | rdm:isPreviousVersionOf                                                                                        |
| ------------------ | -------------------------------------------------------------------------------------------------------------- |
| URI                | https://purl.org/rdm/ontology/isPreviousVersionOf                                                              |
| rdf:type           | ObjectProperty                                                                                                 |
| rdfs:subPropertyOf | rdm:isRelatedTo                                                                                                |
| rdfs:comment       | A Class which is a previous edition of this Class.<br>主語クラスが旧版に当たる、新版のクラス                   |
| owl:inverseOf      | rdm:isNewVersionOf                                                                                             |
| rdfs:domain        | rdm:Resource, rdm:Collection, rdm:SoftwareApplication                                                          |
| rdfs:range         | rdm:Resource, rdm:Collection, rdm:SoftwareApplication                                                          |
| rdfs:seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#ispreviousversionof |

|                    | rdm:isPublishedIn                                                                                              |
| ------------------ | -------------------------------------------------------------------------------------------------------------- |
| URI                | https://purl.org/rdm/ontology/isPublishedIn                                                                    |
| rdf:type           | ObjectProperty                                                                                                 |
| rdfs:subPropertyOf | rdm:isRelatedTo                                                                                                |
| rdfs:comment       | A Class which is published in this Class.<br>主語クラスをその一部として公開するクラス                          |
| rdfs:domain        | rdm:Resource, rdm:Collection, rdm:SoftwareApplication, rdm:Project                                             |
| rdfs:seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#ispreviousversionof |

|                    | rdm:isReferencedBy                                                                                        |
| ------------------ | --------------------------------------------------------------------------------------------------------- |
| URI                | https://purl.org/rdm/ontology/isReferencedBy                                                              |
| rdf:type           | ObjectProperty                                                                                            |
| rdfs:subPropertyOf | rdm:isRelatedTo                                                                                           |
| rdfs:comment       | A Class which uses this Class as a source of information.<br>主語クラスを情報源として参照しているクラス   |
| owl:inverseOf      | rdm:references                                                                                            |
| rdfs:domain        | rdm:Resource, rdm:Collection, rdm:SoftwareApplication, rdm:Project                                        |
| rdfs:seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#isreferencedby |

|                    | rdm:isRequiredBy                                                                                        |
| ------------------ | ------------------------------------------------------------------------------------------------------- |
| URI                | https://purl.org/rdm/ontology/isRequiredBy                                                              |
| rdf:type           | ObjectProperty                                                                                          |
| rdfs:subPropertyOf | rdm:isRelatedTo                                                                                         |
| rdfs:comment       | A Class which requires this Class.<br>主語クラスを必要とするクラス                                      |
| owl:inverseOf      | rdm:requires                                                                                            |
| rdfs:domain        | rdm:Resource, rdm:SoftwareApplication                                                                   |
| rdfs:seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#isrequiredby |

|                    | rdm:isReviewedBy                                                                                        |
| ------------------ | ------------------------------------------------------------------------------------------------------- |
| URI                | https://purl.org/rdm/ontology/isReviewdBy                                                               |
| rdf:type           | ObjectProperty                                                                                          |
| rdfs:subPropertyOf | rdm:isRelatedTo                                                                                         |
| rdfs:comment       | A Class which is a review of this Class.<br>主語クラスのレビューとなっているクラス                      |
| owl:inverseOf      | rdm:reviews                                                                                             |
| rdfs:domain        | rdm:Resource, rdm:SoftwareApplication                                                                   |
| rdfs:seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#isreviewedby |

|                    | rdm:isSourceOf                                                                                        |
| ------------------ | ----------------------------------------------------------------------------------------------------- |
| URI                | https://purl.org/rdm/ontology/isSourceOf                                                              |
| rdf:type           | ObjectProperty                                                                                        |
| rdfs:subPropertyOf | rdm:isRelatedTo                                                                                       |
| rdfs:comment       | A Class from which this Class is derived.<br>主語クラスが基となっているクラス                         |
| owl:inverseOf      | rdm:isDerivedFrom                                                                                     |
| rdfs:domain        | rdm:Project, rdm:Resource, rdm:Collection                                                             |
| rdfs:range         | rdm:Project, rdm:Resource, rdm:Collection                                                             |
| rdfs:seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#issourceof |

|                    | rdm:isSupplementTo                                                                                        |
| ------------------ | --------------------------------------------------------------------------------------------------------- |
| URI                | https://purl.org/rdm/ontology/isSupplementTo                                                              |
| rdf:type           | ObjectProperty                                                                                            |
| rdfs:subPropertyOf | rdm:isRelatedTo                                                                                           |
| rdfs:comment       | A Class that supplements this Class.<br>主語クラスが補足をしているクラス                                  |
| owl:inverseOf      | rdm:isSupplementedBy                                                                                      |
| rdfs:domain        | rdm:Project, rdm:Resource, rdm:Collection                                                                 |
| rdfs:range         | rdm:Project, rdm:Resource, rdm:Collection                                                                 |
| rdfs:seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#issupplementto |

|                    | rdm:isSupplementedBy                                                                                      |
| ------------------ | --------------------------------------------------------------------------------------------------------- |
| URI                | https://purl.org/rdm/ontology/isSupplementedBy                                                            |
| rdf:type           | ObjectProperty                                                                                            |
| rdfs:subPropertyOf | rdm:isRelatedTo                                                                                           |
| rdfs:comment       | A Class which is supplemented by this Class.<br>主語クラスを補足しているクラス                            |
| owl:inverseOf      | rdm:isSupplementTo                                                                                        |
| rdfs:domain        | rdm:Project, rdm:Resource, rdm:Collection                                                                 |
| rdfs:range         | rdm:Project, rdm:Resource, rdm:Collection                                                                 |
| rdfs:seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#issupplementby |

|                    | rdm:isVariantFormOf                                                                                        |
| ------------------ | ---------------------------------------------------------------------------------------------------------- |
| URI                | https://purl.org/rdm/ontology/isVariantFormOf                                                              |
| rdf:type           | ObjectProperty                                                                                             |
| rdfs:subPropertyOf | rdm:isRelatedTo                                                                                            |
| rdfs:comment       | A Class which is the original form of this Class.<br>主語クラスのオリジナルであるクラス                    |
| owl:inverseOf      | rdm:isOriginalFormOf                                                                                       |
| rdfs:domain        | rdm:Resource, rdm:SoftwareApplication                                                                      |
| rdfs:seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#isvariantformof |

|                    | rdm:isVersionOf                                                                                        |
| ------------------ | ------------------------------------------------------------------------------------------------------ |
| URI                | https://purl.org/rdm/ontology/isVersionOf                                                              |
| rdf:type           | ObjectProperty                                                                                         |
| rdfs:subPropertyOf | rdm:isRelatedTo                                                                                        |
| rdfs:comment       | A Class which this Class has as an another version.<br>主語クラスが異なるバージョンであるクラス        |
| owl:inverseOf      | rdm:hasVersion                                                                                         |
| rdfs:domain        | rdm:Resource, rdm:Collection, rdm:SoftwareApplication                                                  |
| rdfs:range         | rdm:Resource, rdm:Collection, rdm:SoftwareApplication                                                  |
| rdfs:seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#isversionof |

|                    | rdm:obsoletes                                                                                        |
| ------------------ | ---------------------------------------------------------------------------------------------------- |
| URI                | https://purl.org/rdm/ontology/obsoletes                                                              |
| rdf:type           | ObjectProperty                                                                                       |
| rdfs:subPropertyOf | rdm:isRelatedTo                                                                                      |
| rdfs:comment       | A Class which is replaced by this Class.<br>主語クラスによって置き換えられたクラス                   |
| owl:inverseOf      | rdm:isObsoletedBy                                                                                    |
| rdfs:seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#obsoletes |

|                    | rdm:references                                                                                        |
| ------------------ | ----------------------------------------------------------------------------------------------------- |
| URI                | https://purl.org/rdm/ontology/references                                                              |
| rdf:type           | ObjectProperty                                                                                        |
| rdfs:subPropertyOf | rdm:isRelatedTo                                                                                       |
| rdfs:comment       | A Class which is used as a source of information by this Class.<br>主語クラスの情報源となったクラス   |
| owl:inverseOf      | rdm:isReferencedBy                                                                                    |
| rdfs:domain        | rdm:Resource, rdm:Collection, rdm:SoftwareApplication, rdm:Project                                    |
| rdfs:seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#references |

|                    | rdm:requires                                                                                        |
| ------------------ | --------------------------------------------------------------------------------------------------- |
| URI                | https://purl.org/rdm/ontology/requires                                                              |
| rdf:type           | ObjectProperty                                                                                      |
| rdfs:subPropertyOf | rdm:isRelatedTo                                                                                     |
| rdfs:comment       | A Class which is required by this Class.<br>主語クラスを必要とするクラス                            |
| owl:inverseOf      | rdm:isRequiredBy                                                                                    |
| rdfs:seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#requires |

|                    | rdm:reviews                                                                                        |
| ------------------ | -------------------------------------------------------------------------------------------------- |
| URI                | https://purl.org/rdm/ontology/reviews                                                              |
| rdf:type           | ObjectProperty                                                                                     |
| rdfs:subPropertyOf | rdm:isRelatedTo                                                                                    |
| rdfs:comment       | A Class which is reviewed by this Class.<br>主語クラスによってレビューされたクラス                 |
| owl:inverseOf      | rdm:isReviewedBy                                                                                   |
| rdfs:domain        | rdm:Resource,, rdm:SoftwareApplication                                                             |
| rdfs:seeAlso       | https://datacite-metadata-schema.readthedocs.io/en/4.5/appendices/appendix-1/relationType/#reviews |

|              | rdm:item                                                                                      |
| ------------ | --------------------------------------------------------------------------------------------- |
| URI          | https://purl.org/rdm/ontology/item                                                            |
| rdf:type     | ObjectProperty                                                                                |
| rdfs:comment | A Resource included in/within this Class.<br>主語クラスに含まれる、もしくは内部にあるリソース |
| rdfs:range   | rdm:Resource                                                                                  |

|                    | rdm:collectionItem                                                        |
| ------------------ | ------------------------------------------------------------------------- |
| URI                | https://purl.org/rdm/ontology/collectionItem                              |
| rdf:type           | ObjectProperty                                                            |
| rdfs:subPropertyOf | rdm:item                                                                  |
| rdfs:comment       | A Resource included in this Collection.<br>コレクションに含まれるリソース |
| owl:inverseOf      | rdm:collectedIn                                                           |
| rdfs:domain        | rdm:Collection                                                            |
| rdfs:range         | rdm:Resource                                                              |

|                    | rdm:projectItem                                                   |
| ------------------ | ----------------------------------------------------------------- |
| URI                | https://purl.org/rdm/ontology/projectItem                         |
| rdf:type           | ObjectProperty                                                    |
| rdfs:subPropertyOf | rdm:item                                                          |
| rdfs:comment       | A Resource within this Project.<br>プロジェクトに含まれるリソース |
| owl:inverseOf      | rdm:inProject                                                     |
| rdfs:domain        | rdm:Project                                                       |
| rdfs:range         | rdm:Resource                                                      |

|                    | rdm:storedItem                                                          |
| ------------------ | ----------------------------------------------------------------------- |
| URI                | https://purl.org/rdm/ontology/storedItem                                |
| rdf:type           | ObjectProperty                                                          |
| rdfs:subPropertyOf | rdm:item                                                                |
| rdfs:comment       | A Resource stored in this Repository.<br>リポジトリに保存されている資源 |
| owl:inverseOf      | rdm:storedIn                                                            |
| rdfs:domain        | rdm:Repository                                                          |
| rdfs:range         | rdm:Resource                                                            |

|                    | rdm:dmpTargetItem                                                             |
| ------------------ | ----------------------------------------------------------------------------- |
| URI                | https://purl.org/rdm/ontology/dmpTargetItem                                   |
| rdf:type           | ObjectProperty                                                                |
| rdfs:subPropertyOf | rdm:item                                                                      |
| rdfs:comment       | A Resource described in DataManagementPlan.<br>DMP で対象になっているリソース |
| rdfs:domain        | rdm:DataManagementPlan                                                        |
| rdfs:range         | rdm:Resource                                                                  |

|              | rdm:licenseInformation                                                          |
| ------------ | ------------------------------------------------------------------------------- |
| URI          | https://purl.org/rdm/ontology/licenseInformation                                |
| rdf:type     | ObjectProperty                                                                  |
| rdfs:comment | Information on license of this Class.<br>プロジェクトやリソースのライセンス情報 |
| rdfs:domain  | rdm:Resource, rdm:Project                                                       |
| rdfs:range   | rdm:License                                                                     |

|                    | rdm:dataLicenseInformation                                                                                 |
| ------------------ | ---------------------------------------------------------------------------------------------------------- |
| URI                | https://purl.org/rdm/ontology/dataLicenseInformation                                                       |
| rdf:type           | ObjectProperty                                                                                             |
| rdfs:subPropertyOf | rdm:licenseInformation                                                                                     |
| rdfs:comment       | The license of research data to be described in this DataManagementPlan.<br>DMP におけるデータのライセンス |
| rdfs:domain        | rdm:DataManagementPlan                                                                                     |

|              | rdm:material                                                                   |
| ------------ | ------------------------------------------------------------------------------ |
| URI          | https://purl.org/rdm/ontology/material                                         |
| rdf:type     | ObjectProperty                                                                 |
| rdfs:comment | Materials and inputs in this Experiment.<br>実験における、材料や入力となるもの |
| rdfs:domain  | rdm:Experiment                                                                 |

|              | rdm:protocol                                               |
| ------------ | ---------------------------------------------------------- |
| URI          | https://purl.org/rdm/ontology/protocol                     |
| rdf:type     | ObjectProperty                                             |
| rdfs:comment | The protocol of this Experiment.<br>実験のプロトコル、手順 |
| rdfs:domain  | rdm:Experiment                                             |

|              | rdm:recipient                                                                                                     |
| ------------ | ----------------------------------------------------------------------------------------------------------------- |
| URI          | https://purl.org/rdm/ontology/recipient                                                                           |
| rdf:type     | ObjectProperty                                                                                                    |
| rdfs:comment | The recipient of this Activity and the affected party of this Activity.<br>行動を受け取る・行動の影響を受ける相手 |
| rdfs:domain  | rdm:Activity                                                                                                      |
| rdfs:range   | rdm:Person                                                                                                        |

|              | rdm:result                                                                                                 |
| ------------ | ---------------------------------------------------------------------------------------------------------- |
| URI          | https://purl.org/rdm/ontology/result                                                                       |
| rdf:type     | ObjectProperty                                                                                             |
| rdfs:comment | The result produced in this Activity / Experiment.<br>アクションや実験によって生成された新しいエンティティ |
| rdfs:domain  | rdm:Activity, rdm:Experiment                                                                               |
| rdfs:range   | rdm:Resource, rdm:Collection, rdm:Project                                                                  |

|               | rdm:storedIn                                                                                            |
| ------------- | ------------------------------------------------------------------------------------------------------- |
| URI           | https://purl.org/rdm/ontology/storedIn                                                                  |
| rdf:type      | ObjectProperty                                                                                          |
| rdfs:comment  | Repository or storage where this Resource is managed.<br>リソースが管理されているリポジトリやストレージ |
| owl:inverseOf | rdm:storedItem                                                                                          |
| rdfs:domain   | rdm:Resource                                                                                            |
| rdfs:range    | rdm:Repository                                                                                          |

|              | rdm:target                                                                      |
| ------------ | ------------------------------------------------------------------------------- |
| URI          | https://purl.org/rdm/ontology/target                                            |
| rdf:type     | ObjectProperty                                                                  |
| rdfs:comment | The indirect object, or target, of this Activity.<br>アクションの間接的な対象物 |
| rdfs:domain  | rdm:Activity                                                                    |
| rdfs:range   | rdm:Resource                                                                    |

|              | rdm:thumbnail                               |
| ------------ | ------------------------------------------- |
| URI          | https://purl.org/rdm/ontology/thumbnail     |
| rdf:type     | ObjectProperty                              |
| rdfs:comment | A thumbnail of this Resource.<br>サムネイル |
| rdfs:domain  | rdm:Resource                                |
| rdfs:range   | rdm:Image                                   |

|               | rdm:wasGeneratedBy                                                            |
| ------------- | ----------------------------------------------------------------------------- |
| URI           | https://purl.org/rdm/ontology/wasGeneratedBy                                  |
| rdf:type      | ObjectProperty                                                                |
| rdfs:comment  | An Activity which created/generated this Class.<br>主語クラスが生成された行動 |
| owl:inverseOf | rdm:result                                                                    |
| rdfs:domain   | rdm:Resource, rdm:Project, rdm:Collection                                     |
| rdfs:range    | rdm:Activity                                                                  |

### DatatypeProperty

|              | rdm:address                                    |
| ------------ | ---------------------------------------------- |
| URI          | https://purl.org/rdm/ontology/address          |
| rdf:type     | DatatypeProperty                               |
| rdfs:comment | Address of this Institution.<br>研究機関の住所 |
| rdfs:domain  | rdm:Institution                                |
| rdfs:range   | xsd:string                                     |

|              | rdm:contact                                                                                                                                         |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| URI          | https://purl.org/rdm/ontology/contact                                                                                                               |
| rdf:type     | DatatypeProperty                                                                                                                                    |
| rdfs:comment | Contacts for data management organizations and managers to be described in this DataManagementPlan.<br>DMP におけるデータ管理機関・管理者への連絡先 |
| rdfs:domain  | rdm:DataManagementPlan                                                                                                                              |
| rdfs:range   | xsd:string                                                                                                                                          |

|              | rdm:copyright                           |
| ------------ | --------------------------------------- |
| URI          | https://purl.org/rdm/ontology/copyright |
| rdf:type     | DatatypeProperty                        |
| rdfs:comment | A copyright notice.<br>コピーライト表記 |
| rdfs:domain  | rdm:License                             |
| rdfs:range   | xsd:string                              |

|              | rdm:dataNumber                                                                 |
| ------------ | ------------------------------------------------------------------------------ |
| URI          | https://purl.org/rdm/ontology/dataNumber                                       |
| rdf:type     | DatatypeProperty                                                               |
| rdfs:comment | The data number assigned to this DataManagementPlan.<br>DMP におけるデータ No. |
| rdfs:domain  | rdm:DataManagementPlan                                                         |
| rdfs:range   | xsd:nonNegativeInteger                                                         |

|              | rdm:date                              |
| ------------ | ------------------------------------- |
| URI          | https://purl.org/rdm/ontology/date    |
| rdf:type     | DatatypeProperty                      |
| rdfs:comment | A date or datetime.<br>日付または日時 |
| rdfs:range   | xsd:date<br>xsd:dateTime              |

|                    | rdm:dateAvailable                                                                                                 |
| ------------------ | ----------------------------------------------------------------------------------------------------------------- |
| URI                | https://purl.org/rdm/ontology/dateAvailable                                                                       |
| rdf:type           | DatatypeProperty                                                                                                  |
| rdfs:subPropertyOf | rdm:date                                                                                                          |
| rdfs:comment       | Scheduled date of open access of the Resource under the rights of embargoed access.<br>公開猶予の場合の公開予定日 |
| rdfs:domain        | rdm:AccessRights                                                                                                  |
| note               | This property is required when the value of rdm:conditionOfAccess is _rdm:EmbargoedAccess_.                       |

|                    | rdm:dateCreated                                                  |
| ------------------ | ---------------------------------------------------------------- |
| URI                | https://purl.org/rdm/ontology/dateCreated                        |
| rdf:type           | DatatypeProperty                                                 |
| rdfs:subPropertyOf | rdm:date                                                         |
| rdfs:comment       | The date on which this Resource was created.<br>リソースの作成日 |
| rdfs:domain        | rdm:Resource                                                     |

|                    | rdm:dateEnded                                 |
| ------------------ | --------------------------------------------- |
| URI                | https://purl.org/rdm/ontology/dateEnded       |
| rdf:type           | DatatypeProperty                              |
| rdfs:subPropertyOf | rdm:date                                      |
| rdfs:comment       | The end date of this Class.<br>クラスの終了日 |
| rdfs:domain        | rdm:Project, rdm:Event, rdm:Activity          |

|                    | rdm:dateModified                                                                   |
| ------------------ | ---------------------------------------------------------------------------------- |
| URI                | https://purl.org/rdm/ontology/dateModified                                         |
| rdf:type           | DatatypeProperty                                                                   |
| rdfs:subPropertyOf | rdm:date                                                                           |
| rdfs:comment       | The date on which the Resource was most recently modified.<br>リソースの最終更新日 |
| rdfs:domain        | rdm:Resource                                                                       |

|                    | rdm:datePublished                                                          |
| ------------------ | -------------------------------------------------------------------------- |
| URI                | https://purl.org/rdm/ontology/datePublished                                |
| rdf:type           | DatatypeProperty                                                           |
| rdfs:subPropertyOf | rdm:date                                                                   |
| rdfs:comment       | The date on which this Resource was published.<br>リソースの発行日・公開日 |
| rdfs:domain        | rdm:Resource                                                               |

|                    | rdm:dateStarted                                 |
| ------------------ | ----------------------------------------------- |
| URI                | https://purl.org/rdm/ontology/dateStarted       |
| rdf:type           | DatatypeProperty                                |
| rdfs:subPropertyOf | rdm:date                                        |
| rdfs:comment       | The start date of this Class.<br>クラスの開始日 |
| rdfs:domain        | rdm:Project, rdm:Event, rdm:Activity            |

|                    | rdm:dateUpdated                                                                             |
| ------------------ | ------------------------------------------------------------------------------------------- |
| URI                | https://purl.org/rdm/ontology/dateUpdated                                                   |
| rdf:type           | DatatypeProperty                                                                            |
| rdfs:subPropertyOf | rdm:date                                                                                    |
| rdfs:comment       | The date on which this Event information was most recently updated.<br>イベントの内容更新日 |
| rdfs:domain        | rdm:Event                                                                                   |

|                    | rdm:sdDatePublished                                            |
| ------------------ | -------------------------------------------------------------- |
| URI                | https://purl.org/rdm/ontology/sdDatePublished                  |
| rdf:type           | DatatypeProperty                                               |
| rdfs:subPropertyOf | rdm:date                                                       |
| rdfs:comment       | The acquisition date of this Resource.<br>外部ファイルの取得日 |
| rdfs:domain        | rdm:Resource                                                   |

|              | rdm:description                                      |
| ------------ | ---------------------------------------------------- |
| URI          | https://purl.org/rdm/ontology/description            |
| rdf:type     | DatatypeProperty                                     |
| rdfs:comment | A description of this Class.<br>クラスの説明         |
| rdfs:domain  | rdm:Resource, rdm:Repository, rdm:Project, rdm:Grant |
| rdfs:range   | xsd:string                                           |

|                    | rdm:dataAccessRequirements                                                                                                   |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------- |
| URI                | https://purl.org/rdm/ontology/dataAccessRequirements                                                                         |
| rdf:type           | DatatypeProperty                                                                                                             |
| rdfs:subPropertyOf | rdm:description                                                                                                              |
| rdfs:comment       | Conditions and method of access to the Resource under access restrictions.<br>アクセス権が限定公開の場合のアクセス条件と方法 |
| rdfs:domain        | rdm:AccessRights                                                                                                             |
| rdfs:range         | xsd:string                                                                                                                   |

|                    | rdm:dataDescription                                                                                      |
| ------------------ | -------------------------------------------------------------------------------------------------------- |
| URI                | https://purl.org/rdm/ontology/dataDescription                                                            |
| rdf:type           | DatatypeProperty                                                                                         |
| rdfs:subPropertyOf | rdm:description                                                                                          |
| rdfs:comment       | The description of research data to be described in this DataManagementPlan.<br>DMP におけるデータの説明 |
| rdfs:domain        | rdm:DataManagementPlan                                                                                   |

|                    | rdm:measurementTechnique                                                                      |
| ------------------ | --------------------------------------------------------------------------------------------- |
| URI                | https://purl.org/rdm/ontology/measurementTechnique                                            |
| rdf:type           | DatatypeProperty                                                                              |
| rdfs:subPropertyOf | rdm:description                                                                               |
| rdfs:comment       | A technique, method or technology used to create research data.<br>研究データの収集・取得方法 |
| rdfs:domain        | rdm:DataManagementPlan                                                                        |
| rdfs:range         | xsd:string                                                                                    |

|                    | rdm:operatingSystem                                                                                 |
| ------------------ | --------------------------------------------------------------------------------------------------- |
| URI                | https://purl.org/rdm/ontology/operatingSystem                                                       |
| rdf:type           | DatatypeProperty                                                                                    |
| rdfs:subPropertyOf | rdm:description                                                                                     |
| rdfs:comment       | Operating systems supported by this SoftwareApplication.<br>アプリケーションがサポートされている OS |
| rdfs:domain        | rdm:SoftwareApplication                                                                             |
| rdfs:range         | xsd:string                                                                                          |

|                    | rdm:processorRequirements                                                                                        |
| ------------------ | ---------------------------------------------------------------------------------------------------------------- |
| URI                | https://purl.org/rdm/ontology/processorRequirements                                                              |
| rdf:type           | DatatypeProperty                                                                                                 |
| rdfs:subPropertyOf | rdm:description                                                                                                  |
| rdfs:comment       | Processor architecture required to run this SoftwareApplication.<br>アプリケーション実行に必要なプロセッサー要件 |
| rdfs:domain        | rdm:SoftwareApplication                                                                                          |
| rdfs:range         | xsd:string                                                                                                       |

|                    | rdm:protocolText                                                                 |
| ------------------ | -------------------------------------------------------------------------------- |
| URI                | https://purl.org/rdm/ontology/protocolText                                       |
| rdf:type           | DatatypeProperty                                                                 |
| rdfs:subPropertyOf | rdm:description                                                                  |
| rdfs:comment       | A text of protocol of this Experiment.<br>実験のプロトコル、手順を示したテキスト |
| rdfs:domain        | rdm:Experiment                                                                   |

|                    | rdm:purpose                                                                                                                                     |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| URI                | https://purl.org/rdm/ontology/purpose                                                                                                           |
| rdf:type           | DatatypeProperty                                                                                                                                |
| rdfs:subPropertyOf | rdm:description                                                                                                                                 |
| rdfs:comment       | Context of this Event implementation e.g. reasons and backgrounds for implementation.<br>実施に至った理由や背景など、イベント実施のコンテクスト |
| rdfs:domain        | rdm:Event                                                                                                                                       |
| rdfs:range         | xsd:string                                                                                                                                      |

|                    | rdm:readme                                                           |
| ------------------ | -------------------------------------------------------------------- |
| URI                | https://purl.org/rdm/ontology/readme                                 |
| rdf:type           | DatatypeProperty                                                     |
| rdfs:subPropertyOf | rdm:description                                                      |
| rdfs:comment       | A text description as Read Me of this SoftwareApplication.<br>README |
| rdfs:domain        | rdm:SoftwareApplication                                              |

|                    | rdm:softwareRequirements                                                                                    |
| ------------------ | ----------------------------------------------------------------------------------------------------------- |
| URI                | https://purl.org/rdm/ontology/softwareRequirements                                                          |
| rdf:type           | DatatypeProperty                                                                                            |
| rdfs:subPropertyOf | rdm:description                                                                                             |
| rdfs:comment       | Component dependency requirements for this SoftwareApplication.<br>アプリケーションコンポーネントの依存要件 |
| rdfs:domain        | rdm:SoftwareApplication                                                                                     |
| rdfs:range         | xsd:string                                                                                                  |

|                    | rdm:specialRequirements                                                                                        |
| ------------------ | -------------------------------------------------------------------------------------------------------------- |
| URI                | https://purl.org/rdm/ontology/specialRequirements                                                              |
| rdf:type           | DatatypeProperty                                                                                               |
| rdfs:subPropertyOf | rdm:description                                                                                                |
| rdfs:comment       | Other requirements for this SoftwareApplication.<br>他のプロパティに当てはまらないアプリケーションに必要な条件 |
| rdfs:domain        | rdm:SoftwareApplication                                                                                        |
| rdfs:range         | xsd:string                                                                                                     |
| note               | This class can be used only when no other subproperty of description is appropriate.                           |

|                    | rdm:storageRequirements                           |
| ------------------ | ------------------------------------------------- |
| URI                | https://purl.org/rdm/ontology/storageRequirements |
| rdf:type           | DatatypeProperty                                  |
| rdfs:subPropertyOf | rdm:description                                   |
| rdfs:comment       | Storage requirements.<br>ストレージの要件         |
| rdfs:domain        | rdm:SoftwareApplication                           |
| rdfs:range         | xsd:string                                        |

|              | rdm:detailedRole                                                                                                                                                                                                      |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| URI          | https://purl.org/rdm/ontology/detailedRole                                                                                                                                                                            |
| rdf:type     | DatatypeProperty                                                                                                                                                                                                      |
| rdfs:comment | A detailed role of this Person.<br>詳細な役割                                                                                                                                                                         |
| rdfs:domain  | rdm:Person                                                                                                                                                                                                            |
| rdfs:range   | xsd:string                                                                                                                                                                                                            |
| note         | This property is for describing detailed role of a Person. When the role can be categorized to one of the subproperties of rdm:contributor, e.g. creator, it is recommended to use it instead of using this property. |

|              | rdm:detailedType                                                                                                                                                                                            |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| URI          | https://purl.org/rdm/ontology/detailedType                                                                                                                                                                  |
| rdf:type     | DatatypeProperty                                                                                                                                                                                            |
| rdfs:comment | A detailed type of this Resource. <br>詳細な資源タイプ                                                                                                                                                      |
| rdfs:domain  | rdm:Resource                                                                                                                                                                                                |
| rdfs:range   | xsd:string                                                                                                                                                                                                  |
| note         | This property is for describing detailed type of a Resource. When the role can be categorized to one of the subclasses of Resource, e.g. Audio, it is recommended to use it instead of using this property. |

|              | rdm:dmpFormat                                      |
| ------------ | -------------------------------------------------- |
| URI          | https://purl.org/rdm/ontology/dmpFormat            |
| rdf:type     | DatatypeProperty                                   |
| rdfs:comment | A name of DataManagementPlan format.<br>DMP 種別名 |
| rdfs:domain  | rdm:DataManagementPlan                             |
| rdfs:range   | xsd:string                                         |

|              | rdm:email                           |
| ------------ | ----------------------------------- |
| URI          | https://purl.org/rdm/ontology/email |
| rdf:type     | DatatypeProperty                    |
| rdfs:comment | Email address.<br>メールアドレス    |
| rdfs:domain  | rdm:Person                          |
| rdfs:range   | xsd:string                          |

|              | rdm:encodingFormat                                        |
| ------------ | --------------------------------------------------------- |
| URI          | https://purl.org/rdm/ontology/encodingFormat              |
| rdf:type     | DatatypeProperty                                          |
| rdfs:comment | A MIME format of this Resource.<br>リソースのフォーマット |
| rdfs:domain  | rdm:Resource                                              |
| rdfs:range   | xsd:string                                                |
| rdfs:seeAlso | http://www.iana.org/assignments/media-types/              |
| note         | A value MUST be in MIME format.                           |

|                    | rdm:dataEncodingFormat                                                                                            |
| ------------------ | ----------------------------------------------------------------------------------------------------------------- |
| URI                | https://purl.org/rdm/ontology/dataEncodingFormat                                                                  |
| rdf:type           | DatatypeProperty                                                                                                  |
| rdfs:subPropertyOf | rdm:encodingFormat                                                                                                |
| rdfs:comment       | The format of research data to be described in this DataManagementPlan.<br>DMP で記述した研究データのフォーマット |
| rdfs:domain        | rdm:DataManagementPlan                                                                                            |

|              | rdm:field                                                                                                                |
| ------------ | ------------------------------------------------------------------------------------------------------------------------ |
| URI          | https://purl.org/rdm/ontology/field                                                                                      |
| rdf:type     | DatatypeProperty                                                                                                         |
| rdfs:comment | A research field of this Project/Resource.<br>プロジェクト・リソースの主題                                               |
| rdfs:domain  | rdm:Resource, rdm:Project                                                                                                |
| rdfs:range   | one of {ライフサイエンス,情報通信,環境,ナノテク・材料,エネルギー,ものづくり技術,社会基盤,フロンティア,人文・社会,その他} |

|              | rdm:keywords                                           |
| ------------ | ------------------------------------------------------ |
| URI          | https://purl.org/rdm/ontology/keywords                 |
| rdf:type     | DatatypeProperty                                       |
| rdfs:comment | Keywords used to describe this Resource.<br>キーワード |
| rdfs:domain  | rdm:Resource                                           |
| rdfs:range   | xsd:string                                             |

|              | rdm:language                           |
| ------------ | -------------------------------------- |
| URI          | https://purl.org/rdm/ontology/language |
| rdf:type     | DatatypeProperty                       |
| rdfs:comment | The language of this Resource.<br>言語 |
| rdfs:domain  | rdm:Resource                           |
| rdfs:range   | xsd:language                           |

|              | rdm:location                                                                                                |
| ------------ | ----------------------------------------------------------------------------------------------------------- |
| URI          | https://purl.org/rdm/ontology/location                                                                      |
| rdf:type     | DatatypeProperty                                                                                            |
| rdfs:comment | The place where this Event was/will be held or this Resource was created.<br>主語クラスの開催場所・取得場所 |
| rdfs:domain  | rdm:Resource, rdm:Event                                                                                     |
| rdfs:range   | xsd:string                                                                                                  |

|              | rdm:name                                                                                                               |
| ------------ | ---------------------------------------------------------------------------------------------------------------------- |
| URI          | https://purl.org/rdm/ontology/name                                                                                     |
| rdf:type     | DatatypeProperty                                                                                                       |
| rdfs:comment | A name of this Class.<br>主語クラスの名称                                                                              |
| rdfs:domain  | rdm:Resource, rdm:Repository, rdm:Project, rdm:License, rdm:Institution, rdm:Grant, rdm:SoftwareApplication, rdm:Event |
| rdfs:range   | xsd:string                                                                                                             |

|                    | rdm:additionalName                                                                     |
| ------------------ | -------------------------------------------------------------------------------------- |
| URI                | https://purl.org/rdm/ontology/additionalName                                           |
| rdf:type           | DatatypeProperty                                                                       |
| rdfs:subPropertyOf | rdm:name                                                                               |
| rdfs:comment       | An additional name for this Person e.g. middle name.<br>ミドルネームなど、その他の名前 |
| rdfs:domain        | rdm:Person                                                                             |
| note               | This property can be used when rdm:name property already has value.                    |

|                    | rdm:familyName                           |
| ------------------ | ---------------------------------------- |
| URI                | https://purl.org/rdm/ontology/familyName |
| rdf:type           | DatatypeProperty                         |
| rdfs:subPropertyOf | rdm:name                                 |
| rdfs:comment       | Family name.<br>名字                     |
| rdfs:domain        | rdm:Person                               |

|                    | rdm:givenName                           |
| ------------------ | --------------------------------------- |
| URI                | https://purl.org/rdm/ontology/givenName |
| rdf:type           | DatatypeProperty                        |
| rdfs:subPropertyOf | rdm:name                                |
| rdfs:comment       | Given name.<br>ファーストネーム         |
| rdfs:domain        | rdm:Person                              |

|                    | rdm:identifierName                                              |
| ------------------ | --------------------------------------------------------------- |
| URI                | https://purl.org/rdm/ontology/identifierName                    |
| rdf:type           | DatatypeProperty                                                |
| rdfs:subPropertyOf | rdm:name                                                        |
| rdfs:comment       | A name of identifier scheme e.g. DOI.<br>識別子のスキーマ名     |
| rdfs:domain        | rdm:Identifier                                                  |
| note               | It is recommended to use identifier scheme which has namespace. |

|              | rdm:query                                                                       |
| ------------ | ------------------------------------------------------------------------------- |
| URI          | https://purl.org/rdm/ontology/query                                             |
| rdf:type     | DatatypeProperty                                                                |
| rdfs:comment | The query used on the Search activity.<br>Search クラスで検索時に使われたクエリ |
| rdfs:domain  | rdm:Search                                                                      |
| rdfs:range   | xsd:string                                                                      |

|              | rdm:size                                                                                                                                 |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------- |
| URI          | https://purl.org/rdm/ontology/size                                                                                                       |
| rdf:type     | DatatypeProperty                                                                                                                         |
| rdfs:comment | This Resource size.<br>主語クラスの大きさ、サイズ                                                                                        |
| rdfs:domain  | rdm:Resource                                                                                                                             |
| rdfs:range   | xsd:string<br>xsd:nonNegativeInteger                                                                                                     |
| note         | When the value is in xsd:string and describes file size, numbers MUST be one-byte characters and units MUST be capitalized, e.g. "58GB". |

|                    | rdm:approximateSize                                                                                       |
| ------------------ | --------------------------------------------------------------------------------------------------------- |
| URI                | https://purl.org/rdm/ontology/approximateSize                                                             |
| rdf:type           | DatatypeProperty                                                                                          |
| rdfs:subPropertyOf | rdm:size                                                                                                  |
| rdfs:comment       | Approximate size of research data to be described in this DataManagementPlan.<br>DMP における概略データ量 |
| rdfs:domain        | rdm:DataManagementPlan                                                                                    |
| rdfs:range         | xsd:string                                                                                                |

|                    | rdm:collectionSize                                                                      |
| ------------------ | --------------------------------------------------------------------------------------- |
| URI                | https://purl.org/rdm/ontology/collectionSize                                            |
| rdf:type           | DatatypeProperty                                                                        |
| rdfs:subPropertyOf | rdm:size                                                                                |
| rdfs:comment       | The number of items in this Collection.<br>所定のパッケージに含まれるデータセットの総数 |
| rdfs:domain        | rdm:Collection                                                                          |
| rdfs:range         | xsd:nonNegativeInteger                                                                  |

|              | rdm:textContent                           |
| ------------ | ----------------------------------------- |
| URI          | https://purl.org/rdm/ontology/textContent |
| rdf:type     | DatatypeProperty                          |
| rdfs:comment | A text.<br>Resource の内容であるテキスト  |
| rdfs:domain  | rdm:Resource                              |
| rdfs:range   | xsd:string                                |

|              | rdm:url                                                       |
| ------------ | ------------------------------------------------------------- |
| URI          | https://purl.org/rdm/ontology/url                             |
| rdf:type     | DatatypeProperty                                              |
| rdfs:comment | A URL related to this Class.<br>主語クラスに関連する URL      |
| rdfs:domain  | rdm:Resource, Repository, Project, License, Grant, Identifier |
| rdfs:range   | xsd:anyURI                                                    |

|              | rdm:value                                                                                                      |
| ------------ | -------------------------------------------------------------------------------------------------------------- |
| URI          | https://purl.org/rdm/ontology/value                                                                            |
| rdf:type     | DatatypeProperty                                                                                               |
| rdfs:comment | A higer-level property that indicates some value of Classes.<br>クラスにおける何かしらの値を示す上位プロパティ |
| rdfs:range   | xsd:anyURI<br>xsd:string<br>xsd:integer<br>xsd:double                                                          |

|                    | rdm:hashValue                                                                                        |
| ------------------ | ---------------------------------------------------------------------------------------------------- |
| URI                | https://purl.org/rdm/ontology/hashValue                                                              |
| rdf:type           | DatatypeProperty                                                                                     |
| rdfs:subPropertyOf | rdm:value                                                                                            |
| rdfs:comment       | Hash value.<br>ハッシュ値                                                                            |
| rdfs:domain        | rdm:Resource                                                                                         |
| rdfs:range         | xsd:string                                                                                           |
| note               | This class is only used as a super-property of properties in expansion such as application profiles. |

|                    | rdm:sha256                                |
| ------------------ | ----------------------------------------- |
| URI                | https://purl.org/rdm/ontology/sha256      |
| rdf:type           | DatatypeProperty                          |
| rdfs:subPropertyOf | rdm:hashValue                             |
| rdfs:comment       | sha256 hash value.<br>sha256 のハッシュ値 |
| rdfs:domain        | rdm:Resource                              |
| rdfs:range         | xsd:string                                |

|                    | rdm:identifierValue                           |
| ------------------ | --------------------------------------------- |
| URI                | https://purl.org/rdm/ontology/identifierValue |
| rdfs:subPropertyOf | rdm:value                                     |
| rdf:type           | DatatypeProperty                              |
| rdfs:comment       | Identifier value.<br>識別子の値               |
| rdfs:domain        | rdm:Identifier                                |
| rdfs:range         | xsd:anyURI<br>xsd:string                      |

|                    | rdm:doi                                                                                                                |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------- |
| URI                | https://purl.org/rdm/ontology/doi                                                                                      |
| rdf:type           | DatatypeProperty                                                                                                       |
| rdfs:subPropertyOf | rdm:identifierValue                                                                                                    |
| rdfs:comment       | DOI URL.<br>DOI                                                                                                        |
| rdfs:domain        | rdm:Resource, rdm:Repository                                                                                           |
| rdfs:range         | xsd:anyURI                                                                                                             |
| rdfs:seeAlso       | https://www.doi.org/                                                                                                   |
| note               | This property is a simplified property of identifierValue in the instance of rdm:Identifier with identifierName _DOI_. |

|                    | rdm:eradResearcherNumber                                                                                                            |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------- |
| URI                | https://purl.org/rdm/ontology/eradResearcherNumber                                                                                  |
| rdf:type           | DatatypeProperty                                                                                                                    |
| rdfs:subPropertyOf | rdm:identifierValue                                                                                                                 |
| rdfs:comment       | e-rad researcher number.<br>e-rad 研究者番号                                                                                        |
| rdfs:domain        | rdm:Person                                                                                                                          |
| rdfs:range         | xsd:string                                                                                                                          |
| rdfs:seeAlso       | https://www.e-rad.go.jp/                                                                                                            |
| note               | This property is a simplified property of identifierValue in the instance of rdm:Identifier with identifierName _e-Rad 研究者番号_. |

|                    | rdm:funderId                                                                                                                |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------- |
| URI                | https://purl.org/rdm/ontology/funderId                                                                                      |
| rdf:type           | DatatypeProperty                                                                                                            |
| rdfs:subPropertyOf | rdm:identifierValue                                                                                                         |
| rdfs:comment       | Funder ID.<br>助成機関識別子                                                                                                |
| rdfs:domain        | rdm:FundingAgency                                                                                                           |
| rdfs:range         | xsd:string                                                                                                                  |
| rdfs:seeAlso       | https://www.crossref.org/services/funder-registry/                                                                          |
| note               | This property is a simplified property of identifierValue in the instance of rdm:Identifier with identifierName _funderID_. |

|                    | rdm:isbn                                                                                                                |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------- |
| URI                | https://purl.org/rdm/ontology/isbn                                                                                      |
| rdf:type           | DatatypeProperty                                                                                                        |
| rdfs:subPropertyOf | rdm:identifierValue                                                                                                     |
| rdfs:comment       | ISBN code.<br>ISBN コード                                                                                               |
| rdfs:domain        | rdm:Book                                                                                                                |
| rdfs:range         | xsd:string                                                                                                              |
| note               | This property is a simplified property of identifierValue in the instance of rdm:Identifier with identifierName _ISBN_. |

|                    | rdm:japanGrantNumber                                                                                                              |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------- |
| URI                | https://purl.org/rdm/ontology/japanGrantNumber                                                                                    |
| rdf:type           | DatatypeProperty                                                                                                                  |
| rdfs:subPropertyOf | rdm:identifierValue                                                                                                               |
| rdfs:comment       | Japan grant number.<br>体系的課題番号                                                                                             |
| rdfs:domain        | rdm:Grant                                                                                                                         |
| rdfs:range         | xsd:string                                                                                                                        |
| rdfs:seeAlso       | https://www.nistep.go.jp/archives/53002                                                                                           |
| note               | This property is a simplified property of identifierValue in the instance of rdm:Identifier with identifierName _体系的課題番号_. |

|                    | rdm:localIdentifier                                                                                  |
| ------------------ | ---------------------------------------------------------------------------------------------------- |
| URI                | https://purl.org/rdm/ontology/localIdentifier                                                        |
| rdf:type           | DatatypeProperty                                                                                     |
| rdfs:subPropertyOf | rdm:identifierValue                                                                                  |
| rdfs:comment       | Local identifier.<br>ローカル識別子                                                                  |
| rdfs:domain        | rdm:Resource, rdm:Experiment                                                                         |
| note               | This class is only used as a super-property of properties in expansion such as application profiles. |

|                    | rdm:orcid                                                                                                                   |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------- |
| URI                | https://purl.org/rdm/ontology/orcid                                                                                         |
| rdf:type           | DatatypeProperty                                                                                                            |
| rdfs:subPropertyOf | rdm:identifierValue                                                                                                         |
| rdfs:comment       | ORCID iD.<br>ORCID iD                                                                                                       |
| rdfs:domain        | rdm:Person                                                                                                                  |
| rdfs:range         | xsd:anyURI                                                                                                                  |
| rdfs:seeAlso       | https://orcid.org/                                                                                                          |
| note               | This property is a simplified property of identifierValue in the instance of rdm:Identifier with identifierName _ORCID iD_. |

|                    | rdm:raid                                                                                                                |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------- |
| URI                | https://purl.org/rdm/ontology/raid                                                                                      |
| rdf:type           | DatatypeProperty                                                                                                        |
| rdfs:subPropertyOf | rdm:identifierValue                                                                                                     |
| rdfs:comment       | RAiD.<br>RAiD                                                                                                           |
| rdfs:domain        | rdm:Project                                                                                                             |
| rdfs:range         | xsd:string                                                                                                              |
| rdfs:seeAlso       | https://raid.org/                                                                                                       |
| note               | This property is a simplified property of identifierValue in the instance of rdm:Identifier with identifierName _RAiD_. |

|                    | rdm:ror                                                                                                                   |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------- |
| URI                | https://purl.org/rdm/ontology/ror                                                                                         |
| rdf:type           | DatatypeProperty                                                                                                          |
| rdfs:subPropertyOf | rdm:identifierValue                                                                                                       |
| rdfs:comment       | ROR ID.<br>ROR ID                                                                                                         |
| rdfs:domain        | rdm:Institution                                                                                                           |
| rdfs:range         | xsd:anyURI                                                                                                                |
| rdfs:seeAlso       | https://ror.org/                                                                                                          |
| note               | This property is a simplified property of identifierValue in the instance of rdm:Identifier with identifierName _ROR ID_. |

|              | rdm:version                              |
| ------------ | ---------------------------------------- |
| URI          | https://purl.org/rdm/ontology/version    |
| rdf:type     | DatatypeProperty                         |
| rdfs:comment | The version of this Class.<br>バージョン |
| rdfs:domain  | rdm:Resource, rdm:SoftwareApplication    |
| rdfs:range   | <br>xsd:string<br>xsd:nonNegativeInteger |

## Named Individuals

|              | rdm:EmbargoedAccess                                                                                      |
| ------------ | -------------------------------------------------------------------------------------------------------- |
| URI          | https://purl.org/rdm/ontology/EmbargoedAccess                                                            |
| rdf:type     | rdm:RightsStatement                                                                                      |
| rdfs:comment | Embargoed access (metadata only access until released for open access on a certain date)<br>公開期間猶予 |
| rdfs:sameAs  | http://purl.org/coar/access_right/c_f1cf                                                                 |

|              | rdm:MetadataOnlyAccess                           |
| ------------ | ------------------------------------------------ |
| URI          | https://purl.org/rdm/ontology/MetadataOnlyAccess |
| rdf:type     | rdm:RightsStatement                              |
| rdfs:comment | Metadata only access.<br>メタデータのみ公開      |
| rdfs:sameAs  | http://purl.org/coar/access_right/c_14cb         |

|              | rdm:OpenAccess                           |
| ------------ | ---------------------------------------- |
| URI          | https://purl.org/rdm/ontology/OpenAccess |
| rdf:type     | rdm:RightsStatement                      |
| rdfs:comment | Open access.<br>公開                     |
| rdfs:sameAs  | http://purl.org/coar/access_right/c_abf2 |

|              | rdm:RestrictedAccess                           |
| ------------ | ---------------------------------------------- |
| URI          | https://purl.org/rdm/ontology/RestrivtedAccess |
| rdf:type     | rdm:RightsStatement                            |
| rdfs:comment | Restricted access.<br>限定公開                 |
| rdfs:sameAs  | http://purl.org/coar/access_right/c_16ec       |

# Usage Guideline

## Identifier

rdm:Identifier class is to describe unique identifier. An identifier system described in this class MUST have its own namespace and be properly managed. Therefore, this class requires the following properties:_rdm:identifierName_, _rdm:identifierManager_ and _rdm:identifierValue_.

### Subproperties of identifierValue

RDM Ontology provides some properties of a particular identifier system for simplicity.

````:JSON
{
  "@context":{
    "@vocab":"https://purl.org/rdm/ontology/"
  }
  "@type": "Resource",
  "identifierInformation":{
    "@type": "Identifier",
    "identifierValue":"https://doi.org/xxxxxxxxxxx",
    "identifierName":"DOI",
    "url":"https://www.doi.org/"
    "identifierManager": {
      "@type":"Institution",
      "name":"The DOI foundation",
      "url":"https://www.doi.org/"
    }
  }
}
```:JSON
The DOI identifier can be described by rdm:Identifier class as above. In contrast, the description by _rdm:doi_ property is simpler:
```:JSON
{
  "@context":{
    "@vocab":"https://purl.org/rdm/ontology/"
  }
  "@type": "Resource",
  "doi":"https://doi.org/xxxxxxxxxxx"
}
````

This is correspondence table for the properties that is subproperty of rdm:identifierValue and its description by using rdm:Identifier class.

| property                 | Identifier.identifierName              | Identifier.url                                     | Identifier.identifierManager.name  | Identifier.identifierManager.url    |
| ------------------------ | -------------------------------------- | -------------------------------------------------- | ---------------------------------- | ----------------------------------- |
| rdm:doi                  | DOI                                    | https://www.doi.org/                               | The DOI foundation                 |                                     |
| rdm:eradResearcherNumber | e-rad 研究者番号@ja                    |                                                    | Cabinet Office,Government of Japan | https://www.e-rad.go.jp/            |
| rdm:funderId             | Open Funder Registry Funder Identifier | https://www.crossref.org/services/funder-registry/ | Crossref                           | https://www.crossref.org/           |
| rdm:isbn                 | International Standard Book Number     |                                                    | International ISBN Agency          | https://www.isbn-international.org/ |
| rdm:japanGrantNumber     | 体系的課題番号@ja                      |                                                    | NISTEP                             | https://www.nistep.go.jp/           |
| rdm:orcid                | ORCID iD                               |                                                    | ORCID, Inc.                        | https://orcid.org/                  |
| rdm:raid                 | RAiD                                   | https://raid.org/                                  | Australian Research Data Commons   | https://ardc.edu.au/                |
| rdm:ror                  | ROR ID                                 | https://ror.org/                                   | ROR                                |

## Value of Field Property

The value of rdm:field is from e-Rad research field. This enumeration list could change based on update of e-Rad definition.

## Class Relationship

Two super-property is defined in RDM Ontology to describe relationship between instances (including instances of same class):rdm:inclusionRelation and rdm:isRelatedTo.
![Figure](class_relationship.png)
