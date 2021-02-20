import React from "react";
import clsx from "clsx";
import Layout from "@theme/Layout";
import Link from "@docusaurus/Link";
import useDocusaurusContext from "@docusaurus/useDocusaurusContext";
import useBaseUrl from "@docusaurus/useBaseUrl";
import useThemeContext from "@theme/hooks/useThemeContext";
import styles from "./styles.module.css";

const features = [
  {
    title: "Easy to Use",
    imageUrl: "img/testtubes.svg",
    description: (
      <>
        Keep track of whats inside each well with confidence through transfers,
        dispensions and aspirations from comprehensivly unit-tested software
      </>
    ),
  },
  {
    title: "One Class for all",
    imageUrl: "img/screens.svg",
    description: (
      <>
        One class for all plates of all sizes with practical deadspace and
        overflow warnings to avoid software errors within lab automation
      </>
    ),
  },
  {
    title: "Wide Range of Utilites",
    imageUrl: "img/web_code.svg",
    description: (
      <>
        In addition to this package's singular class within{" "}
        <code>plateUtils</code> there's a wide range of handy functions for
        common plate software applications
      </>
    ),
  },
];

function Feature({ imageUrl, title, description }) {
  const imgUrl = useBaseUrl(imageUrl);
  return (
    <div className={clsx("col col--4", styles.feature)}>
      {imgUrl && (
        <div className="text--center">
          <img className={styles.featureImage} src={imgUrl} alt={title} />
        </div>
      )}
      <h3>{title}</h3>
      <p>{description}</p>
    </div>
  );
}

function DynamicTitle() {
  const { isDarkTheme } = useThemeContext();
  if (!isDarkTheme) {
    return <img src={"img/whitelogo.svg"} height={"110px"} />;
  } else {
    return <img src={"img/blacklogo.svg"} height={"110px"} />;
  }
}

function Home() {
  const context = useDocusaurusContext();
  const { siteConfig = {} } = context;
  return (
    <Layout
      title={`${siteConfig.title}`}
      description="Description will go into a meta tag in <head />"
    >
      <header className={clsx("hero hero--primary", styles.heroBanner)}>
        <div className="container">
          <h1 className="hero__title">
            <DynamicTitle />
          </h1>
          <p className="hero__subtitle">
            A simple and small class to handle microplate's / micro titreplate's
          </p>
          <div className={styles.buttons}>
            <Link
              className={clsx(
                "button button--outline button--secondary button--lg",
                styles.getStarted
              )}
              to={useBaseUrl("docs/")}
            >
              Get Started
            </Link>
          </div>
        </div>
      </header>
      <main>
        {features && features.length > 0 && (
          <section className={styles.features}>
            <div className="container">
              <div className="row">
                {features.map((props, idx) => (
                  <Feature key={idx} {...props} />
                ))}
              </div>
            </div>
          </section>
        )}
      </main>
    </Layout>
  );
}

export default Home;
