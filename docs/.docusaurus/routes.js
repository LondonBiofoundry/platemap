
import React from 'react';
import ComponentCreator from '@docusaurus/ComponentCreator';
export default [
{
  path: '/platemap/',
  component: ComponentCreator('/platemap/','d59'),
  exact: true,
},
{
  path: '/platemap/blog',
  component: ComponentCreator('/platemap/blog','d52'),
  exact: true,
},
{
  path: '/platemap/blog/hello-world',
  component: ComponentCreator('/platemap/blog/hello-world','7ce'),
  exact: true,
},
{
  path: '/platemap/blog/hola',
  component: ComponentCreator('/platemap/blog/hola','9d2'),
  exact: true,
},
{
  path: '/platemap/blog/tags',
  component: ComponentCreator('/platemap/blog/tags','2e3'),
  exact: true,
},
{
  path: '/platemap/blog/tags/docusaurus',
  component: ComponentCreator('/platemap/blog/tags/docusaurus','b86'),
  exact: true,
},
{
  path: '/platemap/blog/tags/facebook',
  component: ComponentCreator('/platemap/blog/tags/facebook','85f'),
  exact: true,
},
{
  path: '/platemap/blog/tags/hello',
  component: ComponentCreator('/platemap/blog/tags/hello','76a'),
  exact: true,
},
{
  path: '/platemap/blog/tags/hola',
  component: ComponentCreator('/platemap/blog/tags/hola','1d8'),
  exact: true,
},
{
  path: '/platemap/blog/welcome',
  component: ComponentCreator('/platemap/blog/welcome','85b'),
  exact: true,
},
{
  path: '/platemap/docs',
  component: ComponentCreator('/platemap/docs','5a0'),
  
  routes: [
{
  path: '/platemap/docs/',
  component: ComponentCreator('/platemap/docs/','2da'),
  exact: true,
},
{
  path: '/platemap/docs/creating_plates_1',
  component: ComponentCreator('/platemap/docs/creating_plates_1','1f1'),
  exact: true,
},
{
  path: '/platemap/docs/doc2',
  component: ComponentCreator('/platemap/docs/doc2','6a3'),
  exact: true,
},
{
  path: '/platemap/docs/doc3',
  component: ComponentCreator('/platemap/docs/doc3','54f'),
  exact: true,
},
{
  path: '/platemap/docs/installation',
  component: ComponentCreator('/platemap/docs/installation','39d'),
  exact: true,
},
{
  path: '/platemap/docs/mdx',
  component: ComponentCreator('/platemap/docs/mdx','b4b'),
  exact: true,
},
{
  path: '/platemap/docs/reference/platemap/plate',
  component: ComponentCreator('/platemap/docs/reference/platemap/plate','c65'),
  exact: true,
},
{
  path: '/platemap/docs/reference/platemap/PlateUtils/add_volume',
  component: ComponentCreator('/platemap/docs/reference/platemap/PlateUtils/add_volume','f23'),
  exact: true,
},
{
  path: '/platemap/docs/reference/platemap/PlateUtils/remove_volume',
  component: ComponentCreator('/platemap/docs/reference/platemap/PlateUtils/remove_volume','735'),
  exact: true,
},
{
  path: '/platemap/docs/reference/platemap/PlateUtils/transfer',
  component: ComponentCreator('/platemap/docs/reference/platemap/PlateUtils/transfer','86d'),
  exact: true,
},
]
},
{
  path: '*',
  component: ComponentCreator('*')
}
];
