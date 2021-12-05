
import React from 'react';
import ComponentCreator from '@docusaurus/ComponentCreator';
export default [
{
  path: '/',
  component: ComponentCreator('/','deb'),
  exact: true,
},
{
  path: '/__docusaurus/debug',
  component: ComponentCreator('/__docusaurus/debug','3d6'),
  exact: true,
},
{
  path: '/__docusaurus/debug/config',
  component: ComponentCreator('/__docusaurus/debug/config','914'),
  exact: true,
},
{
  path: '/__docusaurus/debug/content',
  component: ComponentCreator('/__docusaurus/debug/content','c28'),
  exact: true,
},
{
  path: '/__docusaurus/debug/globalData',
  component: ComponentCreator('/__docusaurus/debug/globalData','3cf'),
  exact: true,
},
{
  path: '/__docusaurus/debug/metadata',
  component: ComponentCreator('/__docusaurus/debug/metadata','31b'),
  exact: true,
},
{
  path: '/__docusaurus/debug/registry',
  component: ComponentCreator('/__docusaurus/debug/registry','0da'),
  exact: true,
},
{
  path: '/__docusaurus/debug/routes',
  component: ComponentCreator('/__docusaurus/debug/routes','244'),
  exact: true,
},
{
  path: '/blog',
  component: ComponentCreator('/blog','e8b'),
  exact: true,
},
{
  path: '/blog/hello-world',
  component: ComponentCreator('/blog/hello-world','a0f'),
  exact: true,
},
{
  path: '/blog/hola',
  component: ComponentCreator('/blog/hola','bff'),
  exact: true,
},
{
  path: '/blog/tags',
  component: ComponentCreator('/blog/tags','dfe'),
  exact: true,
},
{
  path: '/blog/tags/docusaurus',
  component: ComponentCreator('/blog/tags/docusaurus','891'),
  exact: true,
},
{
  path: '/blog/tags/facebook',
  component: ComponentCreator('/blog/tags/facebook','3ef'),
  exact: true,
},
{
  path: '/blog/tags/hello',
  component: ComponentCreator('/blog/tags/hello','f42'),
  exact: true,
},
{
  path: '/blog/tags/hola',
  component: ComponentCreator('/blog/tags/hola','b70'),
  exact: true,
},
{
  path: '/blog/welcome',
  component: ComponentCreator('/blog/welcome','b3a'),
  exact: true,
},
{
  path: '/docs',
  component: ComponentCreator('/docs','4ab'),
  
  routes: [
{
  path: '/docs/',
  component: ComponentCreator('/docs/','0a9'),
  exact: true,
},
{
  path: '/docs/add_volume',
  component: ComponentCreator('/docs/add_volume','c69'),
  exact: true,
},
{
  path: '/docs/contributing_guideline',
  component: ComponentCreator('/docs/contributing_guideline','71d'),
  exact: true,
},
{
  path: '/docs/creating_plates_1',
  component: ComponentCreator('/docs/creating_plates_1','b9a'),
  exact: true,
},
{
  path: '/docs/doc2',
  component: ComponentCreator('/docs/doc2','fd3'),
  exact: true,
},
{
  path: '/docs/doc3',
  component: ComponentCreator('/docs/doc3','e02'),
  exact: true,
},
{
  path: '/docs/mdx',
  component: ComponentCreator('/docs/mdx','955'),
  exact: true,
},
{
  path: '/docs/plate_attributes',
  component: ComponentCreator('/docs/plate_attributes','b67'),
  exact: true,
},
{
  path: '/docs/reference/platemap/plate',
  component: ComponentCreator('/docs/reference/platemap/plate','7e5'),
  exact: true,
},
{
  path: '/docs/reference/platemap/PlateUtils/add_volume',
  component: ComponentCreator('/docs/reference/platemap/PlateUtils/add_volume','26e'),
  exact: true,
},
{
  path: '/docs/reference/platemap/PlateUtils/assign_source_wells',
  component: ComponentCreator('/docs/reference/platemap/PlateUtils/assign_source_wells','343'),
  exact: true,
},
{
  path: '/docs/reference/platemap/PlateUtils/find_next_well',
  component: ComponentCreator('/docs/reference/platemap/PlateUtils/find_next_well','58e'),
  exact: true,
},
{
  path: '/docs/reference/platemap/PlateUtils/parse_echo_volume_survey',
  component: ComponentCreator('/docs/reference/platemap/PlateUtils/parse_echo_volume_survey','a16'),
  exact: true,
},
{
  path: '/docs/reference/platemap/PlateUtils/remove_volume',
  component: ComponentCreator('/docs/reference/platemap/PlateUtils/remove_volume','759'),
  exact: true,
},
{
  path: '/docs/reference/platemap/PlateUtils/transfer',
  component: ComponentCreator('/docs/reference/platemap/PlateUtils/transfer','854'),
  exact: true,
},
{
  path: '/docs/style',
  component: ComponentCreator('/docs/style','533'),
  exact: true,
},
{
  path: '/docs/transfer_volume',
  component: ComponentCreator('/docs/transfer_volume','d1e'),
  exact: true,
},
]
},
{
  path: '*',
  component: ComponentCreator('*')
}
];
